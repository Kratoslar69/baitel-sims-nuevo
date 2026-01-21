# Índice de Archivos del Sistema Baitel SIMs

Este documento describe todos los archivos del proyecto y su función dentro del sistema.

---

## 📁 Archivos de Documentación

| Archivo | Descripción |
| :--- | :--- |
| `RESUMEN_PROYECTO_BAITEL.md` | **Documento Maestro.** Resumen ejecutivo completo con historial, arquitectura, estado actual y fases futuras. |
| `RESUMEN_EJECUTIVO.md` | Resumen ejecutivo original del proyecto con credenciales y arquitectura. |
| `GUIA_RAPIDA.md` | Guía rápida de uso para los usuarios finales del sistema. |
| `MIGRACION_CONTABO.md` | Guía técnica del intento de migración al VPS de Contabo (incluye troubleshooting). |
| `DIAGNOSTICO_FINAL_CONTABO.md` | Diagnóstico técnico final del fallo del VPS de Contabo. |
| `GUIA_NUEVO_VPS.md` | Recomendaciones de proveedores y pasos para configurar un nuevo VPS. |
| `README.md` | README del repositorio de GitHub. |

---

## 🐍 Archivos de Código Python

### Aplicación Principal

| Archivo | Descripción |
| :--- | :--- |
| `Home.py` | Punto de entrada de la aplicación Streamlit. Muestra el logo y la navegación principal. |
| `version.py` | Define la versión actual del sistema (v1.0.0). |

### Módulos de la Aplicación (Páginas)

| Archivo | Descripción |
| :--- | :--- |
| `pages/1_📥_Captura_SIMs.py` | Módulo de captura masiva de ICCIDs desde archivos Excel. |
| `pages/2_👥_Administrar_Distribuidores.py` | Módulo de gestión de distribuidores y visualización de inventario. |
| `pages/3_🔄_Correcciones.py` | Módulo de reasignación masiva de ICCIDs entre distribuidores. |
| `pages/4_📊_Reportes.py` | Dashboard con métricas, gráficas y análisis temporal del inventario. |

### Utilidades y Lógica de Negocio

| Archivo | Descripción |
| :--- | :--- |
| `utils/__init__.py` | Inicializador del paquete de utilidades. |
| `utils/supabase_client.py` | Cliente de conexión a Supabase. Centraliza la autenticación. |
| `utils/distribuidores_db.py` | Funciones CRUD para la tabla `distribuidores`. |
| `utils/envios_db.py` | Funciones CRUD para la tabla `envios` (SIMs). |
| `utils/timezone_config.py` | Configuración de zona horaria (Ciudad de México). |

### Scripts de Soporte

| Archivo | Descripción |
| :--- | :--- |
| `check_reasignacion.py` | Script para verificar el estado de una reasignación masiva. |
| `rollback_reasignacion.py` | Script para revertir una reasignación masiva en caso de error. |

---

## 🐳 Archivos de Despliegue

| Archivo | Descripción |
| :--- | :--- |
| `Dockerfile` | Configuración de Docker para construir la imagen de la aplicación. |
| `requirements.txt` | Lista de dependencias de Python del proyecto. |

---

## 🎨 Archivos de Assets

| Archivo | Descripción |
| :--- | :--- |
| `assets/LOGO_BAIT.png` | Logo corporativo de Baitel (con fondo blanco). Usado en la interfaz de la aplicación. |

---

## 📦 Archivos Críticos para Backup

Para asegurar la continuidad del proyecto, se recomienda mantener copias de seguridad de los siguientes archivos:

1.  **Código Fuente:** Todos los archivos `.py`
2.  **Documentación:** Todos los archivos `.md`
3.  **Configuración:** `requirements.txt`, `Dockerfile`
4.  **Assets:** `assets/LOGO_BAIT.png`

**Nota:** La base de datos está alojada en Supabase Cloud, por lo que no requiere backup local. Sin embargo, se recomienda exportar un dump periódico de la base de datos desde el panel de Supabase.
