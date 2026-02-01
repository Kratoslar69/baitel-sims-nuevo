"""
Información de versión del sistema
"""

VERSION = "1.1.1"
VERSION_DATE = "01/02/2026"
VERSION_NAME = "Claridad y Correcciones"

def get_version_string():
    """Retorna string de versión completo"""
    return f"v{VERSION} - {VERSION_NAME} ({VERSION_DATE})"

def get_version():
    """Retorna solo el número de versión"""
    return VERSION
