"""
Función de rollback para revertir reasignaciones fallidas
"""
from typing import List, Dict
from .supabase_client import get_supabase_client


def rollback_iccids_reasignados(iccids: List[str]) -> Dict:
    """
    Revierte ICCIDs marcados como REASIGNADO a ACTIVO
    
    Args:
        iccids: Lista de ICCIDs a revertir
    
    Returns:
        Dict con resultado de la operación
    """
    supabase = get_supabase_client()
    
    exitosos = 0
    errores = 0
    detalles = []
    
    for iccid in iccids:
        try:
            # Cambiar estatus de REASIGNADO a ACTIVO
            result = supabase.table('envios')\
                .update({'estatus': 'ACTIVO'})\
                .eq('iccid', iccid.strip().upper())\
                .eq('estatus', 'REASIGNADO')\
                .execute()
            
            if result.data:
                exitosos += 1
                detalles.append({
                    'iccid': iccid,
                    'status': 'OK',
                    'mensaje': 'Revertido a ACTIVO'
                })
            else:
                detalles.append({
                    'iccid': iccid,
                    'status': 'WARNING',
                    'mensaje': 'No encontrado o ya estaba ACTIVO'
                })
        except Exception as e:
            errores += 1
            detalles.append({
                'iccid': iccid,
                'status': 'ERROR',
                'mensaje': str(e)
            })
    
    return {
        'exitosos': exitosos,
        'errores': errores,
        'total': len(iccids),
        'detalles': detalles
    }
