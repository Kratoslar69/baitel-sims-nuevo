# Resumen Ejecutivo: Proyecto Baitel SIMs Sistema

**Fecha:** 18 de Diciembre, 2025
**Versión del Documento:** 1.0
**Autor:** Manus AI

---

## 1. Visión General del Proyecto

El **"Baitel SIMs Sistema"** es una aplicación web a medida desarrollada para la gestión integral del inventario de tarjetas SIM de Baitel. Su objetivo principal es proporcionar una plataforma centralizada, robusta y escalable para rastrear la distribución de ICCIDs, monitorear el desempeño de los distribuidores y, en futuras fases, analizar el ciclo de vida completo de las SIMs, desde su asignación hasta su activación y calidad de venta.

El sistema está diseñado para reemplazar procesos manuales, reducir errores de captura y ofrecer una visión clara y en tiempo real de las operaciones de inventario.

## 2. Estatus Actual del Proyecto

**Versión del Software:** `v1.0.0`
**Estado:** **Estable y Operativo**
**Entorno de Despliegue:** **Railway** (a través de Docker)

El proyecto se encuentra en una fase funcional y estable. Todas las características implementadas hasta la fecha han sido probadas y corregidas. El sistema está desplegado y accesible en producción. La última acción realizada fue la integración del logo corporativo en la interfaz de usuario.

## 3. Hitos y Funcionalidades Implementadas

Se ha completado exitosamente la primera fase del desarrollo, logrando los siguientes hitos:

- **Despliegue en Producción:** Se superaron los desafíos iniciales de configuración del entorno en Railway, migrando de `nixpacks` a un `Dockerfile` personalizado para asegurar la compatibilidad con Python 3.11.
- **Gestión de Inventario (CRUD):**
    - **Captura de SIMs:** Módulo para la asignación masiva de ICCIDs a distribuidores.
    - **Gestión de Distribuidores:** Creación, consulta, actualización y eliminación de distribuidores.
    - **Eliminación de ICCIDs:** Funcionalidad para dar de baja ICCIDs del sistema.
- **Módulo de Correcciones Avanzado:**
    - **Reasignación de ICCIDs:** Se corrigió un error crítico que prevenía la reasignación (violación de `UNIQUE constraint`). La lógica fue cambiada de `INSERT` a `UPDATE`, manteniendo un historial de cambios en el campo `observaciones`.
    - **Corrección de Fecha:** Permite ajustar la fecha de envío de un lote.
- **Dashboard y Analítica (Enfoque Mensual):**
    - Se implementaron métricas clave y gráficos que se centran en la data del mes en curso para mayor relevancia operativa.
    - Todas las gráficas (línea/área) fueron convertidas a **gráficos de barras** para una interpretación más clara y directa.
- **Reportes y Búsqueda:**
    - **Análisis de Distribuidores:** Nueva sección para monitorear el estatus de los distribuidores y el crecimiento mensual.
    - **Búsqueda Avanzada:** Filtros para encontrar ICCIDs o distribuidores por múltiples criterios.
- **Mejoras de Usabilidad y UI:**
    - **Paginación Robusta:** Se eliminó el límite de 1000 registros de Supabase implementando una paginación basada en ID, asegurando que todos los datos sean accesibles.
    - **Integración de Logo:** Se agregó el logo corporativo de Baitel en el sidebar, visible en todas las páginas.
    - **Control de Versiones:** Se muestra la versión actual del sistema en el pie de página.
    - **Timezone Correcto:** Se configuró la zona horaria a `America/Mexico_City` para consistencia en los registros de fecha.

## 4. Stack Tecnológico y Herramientas

| Componente | Herramienta/Tecnología | Propósito en el Proyecto |
| :--- | :--- | :--- |
| **Frontend** | Streamlit (Python) | Framework principal para la construcción de la interfaz de usuario web. |
| **Backend & Base de Datos** | Supabase (PostgreSQL) | Provee la base de datos, autenticación y APIs para la persistencia de datos. |
| **Despliegue (Hosting)** | Railway | Plataforma de hosting para la aplicación en producción. |
| **Contenerización** | Docker | Se utiliza para crear un entorno consistente y desplegable en Railway. |
| **Control de Versiones** | Git & GitHub | Repositorio centralizado para el código fuente y seguimiento de cambios. |
| **Lenguaje de Programación** | Python 3.11 | Lenguaje principal para el desarrollo de toda la aplicación. |

## 5. Estructura de Archivos Clave del Proyecto

Para continuar o retomar el desarrollo, es crucial entender la función de los siguientes archivos dentro del repositorio `baitel-sims-nuevo/`:

| Ruta del Archivo | Descripción |
| :--- | :--- |
| `Home.py` | **Punto de entrada principal.** Define la página de inicio (Dashboard), la configuración global de la página y la estructura del sidebar, incluyendo el logo. |
| `pages/` | Directorio que contiene todas las sub-páginas de la aplicación, siguiendo la nomenclatura de Streamlit para la navegación. |
| `pages/1_📥_Captura_SIMs.py` | Lógica de la interfaz para la captura y asignación masiva de SIMs. |
| `pages/2_👥_Administrar_Distribuidores.py` | Contiene el CRUD completo para la gestión de la información de los distribuidores. |
| `pages/3_🔄_Correcciones.py` | Módulo para realizar ajustes en los datos, como reasignaciones de ICCID y correcciones de fecha. |
| `pages/4_📊_Reportes.py` | Genera los reportes de análisis temporal y de desempeño de distribuidores. |
| `utils/` | Directorio con módulos de ayuda y lógica de negocio reutilizable. |
| `utils/supabase_client.py` | **Archivo crítico.** Gestiona la conexión con la base de datos de Supabase. |
| `utils/distribuidores_db.py` | Contiene todas las funciones para interactuar con la tabla `distribuidores` (ej: `get_todos_distribuidores`). |
| `utils/envios_db.py` | Contiene todas las funciones para interactuar con la tabla `envios` (ej: `reasignar_iccid`). |
| `assets/LOGO_BAIT.png` | El archivo de imagen del logo corporativo. |
| `version.py` | Define la variable de la versión actual del software que se muestra en el footer. |
| `Dockerfile` | **Esencial para el despliegue.** Define las instrucciones para construir la imagen de Docker que se ejecuta en Railway. |
| `requirements.txt` | Lista de todas las dependencias de Python necesarias para que el proyecto funcione. |

## 6. Fases Futuras Planificadas

El roadmap definido por el usuario incluye las siguientes fases:

1.  **Módulo de Activaciones:** Integrar reportes de activación para cruzar datos.
2.  **Módulo de Calidad:** Analizar el historial de recargas para medir la calidad de la venta.
3.  **Portal de Distribuidores:** Crear un portal con acceso restringido para que los distribuidores consulten sus propios KPIs.
4.  **Migración a Contabo VPS:** Mover la aplicación de Railway a un Virtual Private Server en Contabo para mayor control y optimización de costos.

## 7. Arquitectura de la Base de Datos (Supabase)

La base de datos está alojada en Supabase y consta de dos tablas principales:

### Tabla: `distribuidores`

Esta tabla almacena la información de todos los distribuidores registrados en el sistema.

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | UUID | Identificador único (Primary Key). |
| `codigo_bt` | TEXT | Código único del distribuidor (ej: BT476, BT668). |
| `nombre` | TEXT | Nombre completo del distribuidor. |
| `plaza` | TEXT | Ciudad o plaza de operación. |
| `telefono` | TEXT | Teléfono de contacto (opcional). |
| `email` | TEXT | Correo electrónico (opcional). |
| `estatus` | TEXT | Estado del distribuidor: `ACTIVO`, `BAJA`, `SUSPENDIDO`. |
| `fecha_alta` | TIMESTAMP | Fecha de registro en el sistema. |
| `fecha_modificacion` | TIMESTAMP | Última modificación del registro. |

### Tabla: `envios`

Esta tabla registra cada asignación de ICCID a un distribuidor.

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | BIGINT | Identificador único (Primary Key, autoincremental). |
| `iccid` | TEXT | Número ICCID de la SIM (UNIQUE constraint). |
| `codigo_bt` | TEXT | Código del distribuidor asignado. |
| `nombre_distribuidor` | TEXT | Nombre del distribuidor (desnormalizado para reportes). |
| `fecha_envio` | DATE | Fecha de asignación. |
| `cantidad` | INTEGER | Cantidad de SIMs en el envío (usualmente 1 por ICCID). |
| `estatus` | TEXT | Estado del ICCID: `ACTIVO`, `BAJA`, `REASIGNADO`. |
| `observaciones` | TEXT | Campo de texto libre para notas, historial de cambios. |
| `distribuidor_id` | UUID | Foreign Key hacia `distribuidores.id`. |

**Constraint Crítico:** La columna `iccid` tiene un constraint `UNIQUE` (`envios_iccid_key`), lo que impide duplicados y fue la causa de un error crítico resuelto en las últimas correcciones.

## 8. Credenciales y Configuración de Supabase

Para que el sistema funcione correctamente, se requiere la configuración de las siguientes variables de entorno o credenciales:

| Variable | Valor | Descripción |
| :--- | :--- | :--- |
| `SUPABASE_URL` | `https://xgeqtuwjrkvevthzbuhy.supabase.co` | URL del proyecto de Supabase. |
| `SUPABASE_KEY` | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` | Service Role Key para acceso completo a la base de datos. |

**Nota de Seguridad:** La Service Role Key debe mantenerse confidencial. En Railway, estas variables están configuradas en el panel de Environment Variables del proyecto.

## 9. Últimas Correcciones y Mejoras Críticas

Durante el desarrollo reciente, se identificaron y resolvieron los siguientes problemas críticos:

### Corrección 1: Error de Reasignación de ICCIDs (Violación de UNIQUE Constraint)

**Problema:** Al intentar reasignar un ICCID de un distribuidor a otro, el sistema intentaba hacer un `INSERT` de un nuevo registro, lo que violaba el constraint `UNIQUE` de la columna `iccid` en la tabla `envios`.

**Solución:** Se modificó la lógica en `utils/envios_db.py` para utilizar un `UPDATE` en lugar de un `INSERT`. Ahora, cuando se reasigna un ICCID, se actualiza el registro existente cambiando el `codigo_bt`, `nombre_distribuidor` y `distribuidor_id`, y se agrega una nota en el campo `observaciones` con el historial del cambio.

**Archivo Modificado:** `utils/envios_db.py` (función `reasignar_iccid`)

### Corrección 2: Límite de Paginación de 1000 Registros

**Problema:** Supabase tiene un límite predeterminado de 1000 registros por consulta. Esto causaba que los reportes y la visualización de datos no mostraran todos los ICCIDs cuando el inventario superaba este número.

**Solución:** Se implementó una paginación basada en el campo `id` (autoincremental) en lugar de `created_at`. Se creó una función `obtener_todos_los_envios_paginados()` que realiza múltiples consultas secuenciales hasta obtener todos los registros.

**Archivo Modificado:** `utils/supabase_client.py`

### Corrección 3: Conversión de Gráficos a Barras

**Problema:** Los gráficos de línea y área en el dashboard eran confusos para el usuario y no transmitían la información de forma clara.

**Solución:** Se convirtieron todos los gráficos de línea/área a **gráficos de barras** utilizando `plotly.express.bar()`.

**Archivos Modificados:** `Home.py`, `pages/4_📊_Reportes.py`

### Corrección 4: Enfoque en Datos del Mes Actual

**Problema:** El dashboard mostraba datos de los últimos 30 días, lo que no siempre coincidía con el mes calendario y dificultaba el análisis mensual.

**Solución:** Se ajustaron todas las consultas para filtrar datos desde el primer día del mes actual (`datetime.now().replace(day=1)`).

**Archivos Modificados:** `Home.py`, `pages/4_📊_Reportes.py`

### Corrección 5: Configuración de Zona Horaria

**Problema:** Las fechas se registraban en UTC, causando discrepancias con la zona horaria local de México.

**Solución:** Se configuró la zona horaria a `America/Mexico_City` en el módulo `utils/timezone_config.py`.

**Archivo Creado:** `utils/timezone_config.py`

### Corrección 6: Eliminación de Herramienta de Rollback Temporal (Rollback)

**Problema:** Se intentó crear una herramienta de rollback avanzada con selección de distribuidores, pero generó errores de importación y caracteres inválidos en el código.

**Solución:** Se realizó un rollback del repositorio Git al commit anterior estable (`2918a82`) y se eliminaron los archivos relacionados (`pages/9_🔧_Rollback_Temporal.py` y `utils/rollback_reasignacion.py`).

**Acción Tomada:** `git reset --hard 2918a82` y eliminación manual de archivos.

## 10. Despliegue en Railway: Configuración Actual

El proyecto está desplegado en Railway utilizando un `Dockerfile` personalizado. La configuración clave es la siguiente:

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Puerto Expuesto:** `8501` (puerto predeterminado de Streamlit)

**Variables de Entorno en Railway:**
- `SUPABASE_URL`
- `SUPABASE_KEY`

**Comando de Inicio:** `streamlit run Home.py --server.port=8501 --server.address=0.0.0.0`

## 11. Repositorio de GitHub

**Nombre del Repositorio:** `baitel-sims-nuevo`
**Propietario:** Kratoslar69
**URL:** `https://github.com/Kratoslar69/baitel-sims-nuevo.git`

El repositorio contiene todo el código fuente, el `Dockerfile`, las dependencias y los assets necesarios para ejecutar el proyecto.

## 12. Próximos Pasos Recomendados

Para continuar el desarrollo del proyecto, se recomienda seguir este orden de prioridades:

1.  **Completar la Migración a Contabo VPS:** Esto reducirá los costos operativos y proporcionará mayor control sobre el servidor. Se requiere configurar Nginx como reverse proxy, certificados SSL con Let's Encrypt, y un proceso de systemd para mantener Streamlit corriendo.
2.  **Implementar el Módulo de Activaciones:** Permitirá cruzar los datos de asignación con los reportes de activación de Baitel.
3.  **Desarrollar el Módulo de Calidad:** Analizar el historial de recargas para medir la calidad de venta de cada distribuidor.
4.  **Crear el Portal de Distribuidores:** Implementar autenticación y roles para que cada distribuidor pueda acceder a su propio dashboard.

## 13. Contacto y Soporte

Para cualquier duda, continuación del desarrollo o soporte técnico, este documento debe servir como referencia completa del estado actual del proyecto. Todos los cambios están documentados en el historial de commits de Git.

---

**Fin del Resumen Ejecutivo**
