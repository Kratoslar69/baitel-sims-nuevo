"""
Cliente de Supabase con reconexión automática
"""

import streamlit as st
from supabase import create_client, Client
import os
from dotenv import load_dotenv

# Cargar variables de entorno (solo para desarrollo local)
load_dotenv()

def _get_credentials():
    """Obtener URL y KEY de variables de entorno o secrets"""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    if not url or not key:
        try:
            url = st.secrets["SUPABASE_URL"]
            key = st.secrets["SUPABASE_KEY"]
        except (KeyError, FileNotFoundError, AttributeError):
            pass
    if not url or not key:
        raise ValueError("SUPABASE_URL y SUPABASE_KEY deben estar configurados")
    return url, key

@st.cache_resource(show_spinner=False)
def _create_client() -> Client:
    """Crear cliente Supabase (cacheado a nivel de proceso)"""
    url, key = _get_credentials()
    return create_client(url, key)

def get_supabase_client() -> Client:
    """
    Obtener cliente de Supabase con reconexión automática.
    Si la conexión está caída, limpia el caché y reconecta.
    """
    try:
        client = _create_client()
        # Ping rápido para verificar conexión activa
        client.table("distribuidores").select("id").limit(1).execute()
        return client
    except Exception:
        # Limpiar caché y reconectar
        _create_client.clear()
        url, key = _get_credentials()
        return create_client(url, key)
