"""
Sistema de Inventario de SIMs - BAITEL
Pagina Principal / Dashboard
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from utils.supabase_client import get_supabase_client
from utils.distribuidores_db import get_estadisticas_distribuidores
from version import get_version_string

st.set_page_config(
    page_title="BAITEL - Sistema de Inventario SIMs",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .big-metric { font-size: 2.5rem; font-weight: bold; color: #1f77b4; }
    .metric-label { font-size: 1rem; color: #666; }
    .success-box { padding:1rem; background:#d4edda; border-left:5px solid #28a745; border-radius:5px; margin:1rem 0; }
    .warning-box { padding:1rem; background:#fff3cd; border-left:5px solid #ffc107; border-radius:5px; margin:1rem 0; }
</style>
""", unsafe_allow_html=True)

st.title("📱 Sistema de Inventario de SIMs - BAITEL")
st.markdown("---")

with st.sidebar:
    st.image("assets/LOGO_BAIT.png", width=150)
    st.markdown("### 🔧 Navegacion")
    st.info("""
    **Funciones disponibles:**
    - 📊 Dashboard (esta pagina)
    - 📥 Captura de SIMs
    - 👥 Administrar Distribuidores
    - 🔄 Correcciones
    - 📈 Reportes
    """)
    st.markdown("---")
    st.markdown(f"**Usuario:** Almacen BAITEL")
    st.markdown(f"**Fecha:** {datetime.now().strftime('%d/%m/%Y')}")

st.subheader("⚡ Acciones Rapidas")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📥 Capturar SIMs", use_container_width=True, type="primary"):
        st.switch_page("pages/1_📥_Captura_SIMs.py")
with col2:
    if st.button("👥 Nuevo Distribuidor", use_container_width=True):
        st.switch_page("pages/2_👥_Administrar_Distribuidores.py")
with col3:
    if st.button("📊 Ver Reportes", use_container_width=True):
        st.switch_page("pages/4_📊_Reportes.py")

st.markdown("---")

@st.cache_data(ttl=300, show_spinner=False)
def get_dashboard_data():
    """
    Dashboard data — cache 5 minutos.
    Usa la vista v_estadisticas_envios para un solo round-trip al obtener conteos.
    """
    try:
        supabase = get_supabase_client()

        # Vista pre-calculada: 1 query para todos los conteos de envios
        stats_view = supabase.table("v_estadisticas_envios").select("*").execute()
        if stats_view.data:
            sv = stats_view.data[0]
            envios_total   = sv.get("total", 0)
            envios_activos = sv.get("activos", 0)
        else:
            envios_total   = supabase.table("envios").select("*", count="exact").execute().count
            envios_activos = supabase.table("envios").select("*", count="exact").eq("estatus_envio", "ACTIVO").execute().count

        # Estadisticas de distribuidores (cacheadas por separado 5 min)
        stats_dist = get_estadisticas_distribuidores()

        # Actividad del mes actual (solo columnas necesarias, con limite)
        primer_dia_mes = datetime.now().replace(day=1).date().isoformat()
        actividad_reciente = supabase.table("envios")            .select("fecha_envio, codigo_bt, iccid")            .gte("fecha_envio", primer_dia_mes)            .execute()

        top_distribuidores = actividad_reciente.data  # reutiliza datos ya traidos

        return {
            "stats_dist":        stats_dist,
            "envios_total":      envios_total,
            "envios_activos":    envios_activos,
            "actividad_reciente": actividad_reciente.data,
            "top_distribuidores": top_distribuidores,
        }
    except Exception as e:
        st.error(f"Error al cargar datos: {str(e)}")
        return None

with st.spinner("Cargando dashboard..."):
    data = get_dashboard_data()

if data:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("👥 Distribuidores Activos", data["stats_dist"]["activos"],
                  delta=f"Total: {data['stats_dist']['total']}")
    with col2:
        st.metric("📱 SIMs Asignadas (Total)", f"{data['envios_total']:,}", delta="Historico completo")
    with col3:
        st.metric("✅ SIMs Activas", f"{data['envios_activos']:,}", delta="En circulacion")
    with col4:
        hoy = datetime.now().date().isoformat()
        actividad_hoy = len([x for x in data["actividad_reciente"] if x.get("fecha_envio","").startswith(hoy)])
        st.metric("📥 Asignaciones Hoy", actividad_hoy, delta="Ultimas 24h")

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Distribucion de Distribuidores")
        fig_dist = go.Figure(data=[go.Pie(
            labels=["Activos","Baja","Suspendidos"],
            values=[data["stats_dist"]["activos"], data["stats_dist"]["baja"], data["stats_dist"]["suspendidos"]],
            hole=.4,
            marker=dict(colors=["#28a745","#dc3545","#ffc107"]),
            textinfo="label+value+percent", textposition="outside"
        )])
        fig_dist.update_layout(showlegend=True, height=350, margin=dict(l=20,r=20,t=30,b=20))
        st.plotly_chart(fig_dist, use_container_width=True)

    with col2:
        mes_actual = datetime.now().strftime("%B %Y")
        st.subheader(f"📈 Actividad de Envios - {mes_actual}")
        primer_dia = datetime.now().replace(day=1).date()
        dia_actual = datetime.now().date()
        todos_los_dias = pd.date_range(start=primer_dia, end=dia_actual, freq="D")
        df_completo = pd.DataFrame({"fecha": todos_los_dias, "cantidad": 0})
        if data["actividad_reciente"]:
            df_act = pd.DataFrame(data["actividad_reciente"])
            df_act["fecha_envio"] = pd.to_datetime(df_act["fecha_envio"]).dt.date
            act_dia = df_act.groupby("fecha_envio").size().reset_index(name="cantidad")
            df_completo["fecha"] = pd.to_datetime(df_completo["fecha"]).dt.date
            for _, row in act_dia.iterrows():
                df_completo.loc[df_completo["fecha"] == row["fecha_envio"], "cantidad"] = row["cantidad"]
        df_completo["fecha"] = pd.to_datetime(df_completo["fecha"])
        fig_act = px.bar(df_completo, x="fecha", y="cantidad", text="cantidad",
                         labels={"fecha":"Fecha","cantidad":"SIMs Asignadas"},
                         color_discrete_sequence=["#1f77b4"])
        fig_act.update_traces(textposition="outside")
        fig_act.update_layout(height=300, margin=dict(l=20,r=20,t=30,b=20),
                              hovermode="x unified",
                              xaxis=dict(tickformat="%d %b", dtick=86400000.0))
        st.plotly_chart(fig_act, use_container_width=True)

    st.markdown("---")
    st.subheader(f"🏆 Top 10 Distribuidores - {mes_actual}")
    if data["top_distribuidores"]:
        df_top = pd.DataFrame(data["top_distribuidores"])
        top_10 = df_top.groupby(["codigo_bt","nombre_distribuidor"]).size()            .reset_index(name="total_sims").sort_values("total_sims", ascending=False).head(10)
        fig_top = px.bar(top_10, x="total_sims", y="codigo_bt", orientation="h",
                         text="total_sims", color_discrete_sequence=["#1f77b4"])
        fig_top.update_layout(height=450, showlegend=False,
                              yaxis={"categoryorder":"total ascending"})
        fig_top.update_traces(textposition="outside", textfont=dict(size=12, color="black"))
        st.plotly_chart(fig_top, use_container_width=True)
    else:
        st.info("Sin datos de envios aun")
else:
    st.error("Error al cargar los datos del dashboard")
    st.info("Verifica tu conexion a Supabase")

st.markdown("---")
version = get_version_string()
st.markdown(f"""
<div style='text-align:center;color:#666;padding:1rem;'>
    <small>Sistema de Inventario de SIMs - BAITEL {version} © 2025</small>
</div>
""", unsafe_allow_html=True)
