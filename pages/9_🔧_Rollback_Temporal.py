"""
Página temporal para hacer rollback de reasignaciones fallidas
"""
import streamlit as st
from utils.rollback_reasignacion import rollback_iccids_reasignados

st.set_page_config(
    page_title="Rollback Temporal",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 Rollback de Reasignaciones Fallidas")

st.warning("⚠️ Esta es una página temporal para corregir el problema de reasignación")

# Lista de ICCIDs a revertir
iccids = [
    "8952140063706448589F",
    "8952140063706448597F",
    "8952140063706448605F",
    "8952140063706448613F",
    "8952140063706448621F",
    "8952140063706448639F",
    "8952140063706448647F",
    "8952140063706448654F",
    "8952140063706448662F",
    "8952140063706448670F",
    "8952140063706448688F",
    "8952140063706448696F",
    "8952140063706448704F",
    "8952140063706448712F",
    "8952140063706448720F",
    "8952140063706448738F",
    "8952140063706448746F",
    "8952140063706448753F",
    "8952140063706448761F",
    "8952140063706448779F",
    "8952140063706448787F",
    "8952140063706448795F",
    "8952140063706448803F",
    "8952140063706448811F",
    "8952140063706448829F",
    "8952140063706448837F",
    "8952140063706448845F",
    "8952140063706448852F",
    "8952140063706448860F",
    "8952140063706448878F"
]

st.info(f"Se revertirán {len(iccids)} ICCIDs de REASIGNADO a ACTIVO")

if st.button("🔄 Ejecutar Rollback", type="primary"):
    with st.spinner("Procesando..."):
        resultado = rollback_iccids_reasignados(iccids)
    
    st.success(f"✅ Rollback completado: {resultado['exitosos']} exitosos, {resultado['errores']} errores")
    
    # Mostrar detalles
    for detalle in resultado['detalles']:
        if detalle['status'] == 'OK':
            st.success(f"✅ {detalle['iccid']}: {detalle['mensaje']}")
        elif detalle['status'] == 'WARNING':
            st.warning(f"⚠️ {detalle['iccid']}: {detalle['mensaje']}")
        else:
            st.error(f"❌ {detalle['iccid']}: {detalle['mensaje']}")
