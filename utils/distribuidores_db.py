"""
Funciones CRUD para la tabla distribuidores
"""

from typing import List, Dict, Optional
from datetime import datetime
from .supabase_client import get_supabase_client
import streamlit as st


def buscar_distribuidores(query: str = "", estatus: Optional[str] = None, limit: int = 100) -> List[Dict]:
    supabase = get_supabase_client()
    db_query = supabase.table("distribuidores").select("*")
    if estatus:
        db_query = db_query.eq("estatus_distribuidor", estatus)
    if query:
        q = query.upper().strip()
        db_query = db_query.or_(
            f"codigo_bt.ilike.%{q}%,nombre.ilike.%{q}%,plaza.ilike.%{q}%"
        )
    db_query = db_query.order("codigo_bt").limit(limit)
    return db_query.execute().data


def get_distribuidor_by_codigo(codigo_bt: str) -> Optional[Dict]:
    supabase = get_supabase_client()
    result = supabase.table("distribuidores").select("*").eq("codigo_bt", codigo_bt.upper().strip()).execute()
    return result.data[0] if result.data else None


def get_distribuidor_by_id(id: str) -> Optional[Dict]:
    supabase = get_supabase_client()
    result = supabase.table("distribuidores").select("*").eq("id", id).execute()
    return result.data[0] if result.data else None


def crear_distribuidor(codigo_bt, nombre, plaza, telefono=None, email=None, estatus="ACTIVO") -> Dict:
    supabase = get_supabase_client()
    data = {
        "codigo_bt": codigo_bt.upper().strip(),
        "nombre": nombre.upper().strip(),
        "plaza": plaza.upper().strip(),
        "estatus_distribuidor": estatus.upper().strip(),
        "fecha_alta": datetime.now().isoformat(),
    }
    if telefono: data["telefono"] = telefono.strip()
    if email:    data["email"] = email.lower().strip()
    return supabase.table("distribuidores").insert(data).execute().data[0]


def actualizar_distribuidor(id: str, **campos) -> Dict:
    supabase = get_supabase_client()
    data = {}
    if "codigo_bt" in campos: data["codigo_bt"] = campos["codigo_bt"].upper().strip()
    if "nombre"   in campos: data["nombre"]    = campos["nombre"].upper().strip()
    if "plaza"    in campos: data["plaza"]     = campos["plaza"].upper().strip()
    if "estatus"  in campos: data["estatus_distribuidor"] = campos["estatus"].upper().strip()
    if "telefono" in campos: data["telefono"]  = campos["telefono"].strip() if campos["telefono"] else None
    if "email"    in campos: data["email"]     = campos["email"].lower().strip() if campos["email"] else None
    data["fecha_modificacion"] = datetime.now().isoformat()
    return supabase.table("distribuidores").update(data).eq("id", id).execute().data[0]


def get_siguiente_codigo_bt() -> str:
    supabase = get_supabase_client()
    result = supabase.table("distribuidores").select("codigo_bt").order("codigo_bt", desc=True).limit(1).execute()
    if not result.data:
        return "BT001-"
    try:
        import re
        match = re.search(r"BT(\d+)", result.data[0]["codigo_bt"])
        if match:
            return f"BT{int(match.group(1)) + 1:03d}-"
    except:
        pass
    return "BT001-"


@st.cache_data(ttl=300, show_spinner=False)
def get_estadisticas_distribuidores() -> Dict:
    """
    Estadisticas en UNA sola query usando RPC SQL.
    Cache 5 minutos.
    """
    supabase = get_supabase_client()
    result = supabase.rpc("get_stats_distribuidores").execute()
    if result.data:
        row = result.data[0]
        return {
            "total":       row.get("total", 0),
            "activos":     row.get("activos", 0),
            "baja":        row.get("baja", 0),
            "suspendidos": row.get("suspendidos", 0),
        }
    # Fallback: 4 queries si la RPC no existe
    total      = supabase.table("distribuidores").select("*", count="exact").execute()
    activos    = supabase.table("distribuidores").select("*", count="exact").eq("estatus_distribuidor", "ACTIVO").execute()
    baja       = supabase.table("distribuidores").select("*", count="exact").eq("estatus_distribuidor", "BAJA").execute()
    suspendidos= supabase.table("distribuidores").select("*", count="exact").eq("estatus_distribuidor", "SUSPENDIDO").execute()
    return {"total": total.count, "activos": activos.count, "baja": baja.count, "suspendidos": suspendidos.count}


def get_todos_distribuidores() -> List[Dict]:
    supabase = get_supabase_client()
    return supabase.table("distribuidores").select("*").order("codigo_bt").execute().data


def eliminar_distribuidor(id: str) -> Dict:
    supabase = get_supabase_client()
    result = supabase.table("distribuidores").delete().eq("id", id).execute()
    return result.data[0] if result.data else None
