"""
Cliente de Supabase con cache
"""

import streamlit as st
from supabase import create_client, Client
import os

# NO cargar dotenv en producción (Railway)
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

@st.cache_resource
def get_supabase_client() -> Client:
    """
    Obtener cliente de Supabase con cache
    Prioriza variables de entorno (Railway), luego secrets de Streamlit
    
    Returns:
        Client: Cliente de Supabase
    """
    # Intentar obtener de variables de entorno primero (Railway, desarrollo local)
    url = os.environ.get("SUPABASE_URL") or os.getenv("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY") or os.getenv("SUPABASE_KEY")
    
    # Si no están en variables de entorno, intentar secrets de Streamlit
    if not url or not key:
        try:
            url = st.secrets["SUPABASE_URL"]
            key = st.secrets["SUPABASE_KEY"]
        except (KeyError, FileNotFoundError, AttributeError):
            pass
    
    if not url or not key:
        raise ValueError(f"SUPABASE_URL y SUPABASE_KEY deben estar configurados. URL encontrada: {bool(url)}, KEY encontrada: {bool(key)}")
    
    return create_client(url, key)
