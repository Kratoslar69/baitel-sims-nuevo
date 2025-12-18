"""
Script para hacer rollback de los ICCIDs marcados como REASIGNADO
"""
import os
from supabase import create_client

def get_supabase_client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    return create_client(url, key)

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

supabase = get_supabase_client()

print(f"\n=== Iniciando rollback de {len(iccids)} ICCIDs ===\n")

exitosos = 0
errores = 0

for iccid in iccids:
    try:
        # Cambiar estatus de REASIGNADO a ACTIVO
        result = supabase.table('envios')\
            .update({'estatus': 'ACTIVO'})\
            .eq('iccid', iccid)\
            .eq('estatus', 'REASIGNADO')\
            .execute()
        
        if result.data:
            print(f"✅ {iccid} - Revertido a ACTIVO")
            exitosos += 1
        else:
            print(f"⚠️ {iccid} - No encontrado o ya estaba ACTIVO")
    except Exception as e:
        print(f"❌ {iccid} - Error: {str(e)}")
        errores += 1

print(f"\n=== Resumen ===")
print(f"Exitosos: {exitosos}")
print(f"Errores: {errores}")
print(f"Total: {len(iccids)}\n")
