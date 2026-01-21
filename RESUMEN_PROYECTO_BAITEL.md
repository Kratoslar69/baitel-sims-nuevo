> **Documento Maestro del Proyecto: Sistema de Gestión de SIMs Baitel**
> **Última Actualización:** 27 de Diciembre de 2025
> **Versión del Sistema:** 1.0.0

# Resumen Ejecutivo y Técnico

Este documento consolida toda la historia, el estado actual, la arquitectura técnica y las fases futuras del proyecto **"Sistema de Gestión de SIMs Baitel"**. Su propósito es servir como una fuente única de verdad para retomar el desarrollo en cualquier momento sin pérdida de contexto.

---

## 1. Visión General del Proyecto

El sistema es una aplicación web interna desarrollada para un distribuidor de Baitel, diseñada para solucionar la necesidad crítica de capturar, administrar y generar reportes sobre grandes volúmenes de ICCIDs (identificadores de tarjetas SIM). La plataforma centraliza el inventario de SIMs, su asignación a distribuidores secundarios y proporciona inteligencia de negocio a través de dashboards.

---

## 2. Estado Actual del Proyecto (Diciembre 2025)

| Componente | Estado | Detalles y Ubicación |
| :--- | :--- | :--- |
| **Sistema Baitel SIMs v1.0.0** | ✅ **100% Operativo** | Desplegado en **Railway**. URL: [https://baitel-sims-nuevo-production.up.railway.app](https://baitel-sims-nuevo-production.up.railway.app) |
| **Base de Datos** | ✅ **Estable y Operativa** | **Supabase Cloud** (PostgreSQL). Contiene **97,806** registros de SIMs. |
| **Código Fuente** | ✅ **Estable** | Repositorio de GitHub: `baitel-sims-nuevo` |
| **VPS Contabo** | ❌ **Fallido / Pendiente Formateo** | El intento de migración al VPS (5.189.174.129) falló debido a inestabilidad de Docker. Se ha decidido formatear el servidor. |

**Conclusión Actual:** El sistema principal se mantiene en producción en Railway, que ha demostrado ser una plataforma robusta y confiable. La migración a un VPS auto-gestionado se pospone hasta que se adquiera y configure un nuevo servidor de un proveedor recomendado (DigitalOcean, Hetzner, etc.).

---

## 3. Arquitectura y Stack Tecnológico

El sistema fue construido con un enfoque en la rapidez de desarrollo y la facilidad de uso, utilizando Python y Streamlit.

- **Lenguaje:** Python 3.11+
- **Framework Frontend:** Streamlit 1.32.0
- **Base de Datos:** Supabase Cloud (PostgreSQL - Plan Pro)
- **Hosting Principal:** Railway
- **Librerías Clave:**
    - `pandas`: Para manipulación de datos en memoria.
    - `openpyxl`: Para la lectura de archivos Excel (`.xlsx`).
    - `plotly`: Para la generación de gráficas interactivas en el dashboard.
    - `supabase-py`: Cliente oficial para la interacción con la base de datos.

### Arquitectura de la Aplicación (Módulos v1.0.0)

La aplicación está estructurada en 4 módulos funcionales accesibles desde una barra lateral:

1.  **📥 Captura SIMs:** Permite la carga masiva de ICCIDs desde un archivo Excel, asignándolos a un distribuidor específico.
2.  **👥 Administrar Distribuidores:** Ofrece un CRUD para la gestión de distribuidores y permite visualizar el inventario de SIMs asignado a cada uno.
3.  **🔄 Correcciones:** Facilita la reasignación masiva de un lote de ICCIDs de un distribuidor a otro, una funcionalidad crítica para corregir errores de asignación.
4.  **📊 Reportes:** Un dashboard completo con métricas clave, análisis de asignaciones por fecha, y gráficas interactivas sobre el inventario total y por distribuidor.

### Arquitectura de la Base de Datos (Supabase)

La estructura es simple y eficiente, centrada en dos tablas principales:

- **`distribuidores`**
    - `id` (PK, autoincremental)
    - `nombre` (texto)
    - `created_at` (timestamp)
- **`envios`**
    - `id` (PK, autoincremental)
    - `iccid` (texto, único)
    - `distribuidor_id` (FK a `distribuidores.id`)
    - `fecha_asignacion` (date)
    - `created_at` (timestamp)

---

## 4. Historial del Proyecto

1.  **Desarrollo de v1.0.0:** Creación de los 4 módulos principales y conexión a Supabase.
2.  **Puesta en Producción:** Despliegue exitoso en la plataforma de Railway.
3.  **Carga Masiva Inicial:** Ingesta de 97,806 SIMs en la base de datos.
4.  **Branding:** Integración del logo corporativo en la interfaz de la aplicación.
5.  **Intento de Migración a Contabo:** Se instaló la aplicación en un VPS de Contabo, se configuró el DNS y un servicio `systemd`.
6.  **Fallo de Migración:** Surgieron conflictos con el firewall de Contabo, Nginx y las aplicaciones Docker Swarm preexistentes del usuario, causando una falla generalizada de servicios (Error 137).
7.  **Diagnóstico y Rollback:** Se diagnosticó una posible corrupción del entorno Docker. Se limpió completamente la aplicación del VPS y se decidió formatear el servidor.
8.  **Decisión Estratégica:** Mantener Railway como solución principal y planificar una futura migración a un proveedor de VPS más confiable.

---

## 5. Fases Futuras (Roadmap del Proyecto)

El proyecto está diseñado para crecer. Las siguientes fases están planificadas para cuando se decida retomar el desarrollo activo:

- **Fase 2: Módulo de Activaciones**
    - **Objetivo:** Cruzar los ICCIDs del inventario con los reportes de activación de Baitel para saber qué SIMs ya han sido vendidas y activadas.
    - **Funcionalidad:** Carga de reportes de activación y actualización de estado de los ICCIDs.

- **Fase 3: Módulo de Calidad y Desempeño**
    - **Objetivo:** Medir la "calidad" de los distribuidores basada en el tiempo que tardan en activar las SIMs y el volumen de recargas.
    - **Funcionalidad:** Dashboards con métricas de desempeño, tiempo promedio de activación y análisis de recargas.

- **Fase 4: Portal de Distribuidores**
    - **Objetivo:** Crear un portal con login individual para que cada distribuidor pueda ver únicamente su propio inventario y métricas.
    - **Funcionalidad:** Sistema de autenticación y vistas personalizadas por usuario.

- **Fase 5: Migración a Nuevo VPS**
    - **Objetivo:** Mover la aplicación de Railway a un VPS auto-gestionado, una vez que el nuevo servidor esté configurado y estable.
    - **Funcionalidad:** Despliegue en Docker Swarm con Traefik para SSL y routing.

---

## 6. Instrucciones para Retomar el Proyecto

Para levantar el entorno de desarrollo localmente o migrar el sistema, sigue estos pasos:

1.  **Clonar el Repositorio:** `git clone <URL_DEL_REPOSITORIO_GIT>`
2.  **Instalar Dependencias:** `pip install -r requirements.txt`
3.  **Configurar Credenciales:** Asegúrate de tener las credenciales de Supabase (URL y Key) disponibles, preferiblemente como variables de entorno.
4.  **Ejecutar la Aplicación:** `streamlit run app.py`
5.  **Conexión a la BD:** La aplicación se conectará automáticamente a la base de datos de Supabase Cloud, por lo que no se requiere una base de datos local.
