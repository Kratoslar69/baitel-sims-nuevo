"""
Sistema de versionado de la aplicación
"""

VERSION = "1.1.0"
VERSION_DATE = "2026-01-21"
VERSION_NAME = "Mejoras en Reportes"

def get_version_info():
    """Retorna información completa de la versión"""
    return {
        'version': VERSION,
        'date': VERSION_DATE,
        'name': VERSION_NAME
    }

def get_version_string():
    """Retorna string formateado de la versión"""
    return f"v{VERSION}"

def get_full_version_string():
    """Retorna string completo con nombre y fecha"""
    return f"v{VERSION} - {VERSION_NAME} ({VERSION_DATE})"
