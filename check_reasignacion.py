import streamlit as st
from utils.supabase_client import get_supabase_client

supabase = get_supabase_client()

# Buscar todos los registros de este ICCID
iccid = "8952140063706448589F"
result = supabase.table('envios')\
    .select('*')\
    .eq('iccid', iccid)\
    .order('created_at', desc=True)\
    .execute()

print(f"\n=== Registros encontrados para {iccid}: {len(result.data)} ===\n")

for idx, registro in enumerate(result.data, 1):
    print(f"Registro #{idx}:")
    print(f"  ID: {registro['id']}")
    print(f"  Código BT: {registro['codigo_bt']}")
    print(f"  Distribuidor: {registro['nombre_distribuidor']}")
    print(f"  Estatus: {registro['estatus']}")
    print(f"  Fecha envío: {registro['fecha_envio']}")
    print(f"  Created at: {registro['created_at']}")
    print(f"  Observaciones: {registro.get('observaciones', 'N/A')}")
    print()
