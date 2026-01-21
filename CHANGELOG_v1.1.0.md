# Changelog - Versión 1.1.0

**Fecha:** 21 de Enero de 2026  
**Nombre:** Mejoras en Reportes

---

## 🎯 Resumen de Cambios

Esta versión introduce mejoras significativas en el módulo de **Reportes** para mejorar la experiencia de usuario y agregar funcionalidades solicitadas.

---

## ✨ Nuevas Funcionalidades

### 1. Botón de Búsqueda en "Por Distribuidor"

**Ubicación:** Módulo de Reportes → Pestaña "Por Distribuidor"

**Problema Resuelto:** Anteriormente, la búsqueda se ejecutaba automáticamente al escribir en el campo de texto, lo que podía generar búsquedas innecesarias.

**Solución Implementada:**
- Se agregó un botón **"🔍 Buscar Distribuidor"** que debe ser presionado para ejecutar la búsqueda.
- Mejora la experiencia de usuario al permitir configurar todos los filtros antes de ejecutar la consulta.

**Código Modificado:**
- Archivo: `pages/4_📊_Reportes.py`
- Línea 288: Agregado botón de búsqueda
- Línea 290: Modificada condición para ejecutar búsqueda solo cuando se presiona el botón

---

### 2. Filtro de Estatus de Distribuidor en "Consulta Personalizada"

**Ubicación:** Módulo de Reportes → Pestaña "Consulta Personalizada"

**Problema Resuelto:** No existía forma de filtrar ICCIDs por el estatus del distribuidor (ACTIVO vs BAJA), solo se podía filtrar por el estatus del envío.

**Solución Implementada:**
- Se renombró el filtro existente a **"Estatus del Envío"** para mayor claridad.
- Se agregó un nuevo filtro **"Estatus del Distribuidor"** con las opciones:
  - **TODOS** (sin filtro)
  - **ACTIVO** (solo distribuidores activos)
  - **BAJA** (solo distribuidores dados de baja)
  - **SUSPENDIDO** (solo distribuidores suspendidos)

**Lógica Implementada:**
1. Primero se ejecuta la búsqueda de envíos con los filtros tradicionales (ICCID, código BT, fechas, estatus del envío).
2. Si se selecciona un estatus de distribuidor específico, se consulta la tabla `distribuidores` para obtener los códigos BT válidos.
3. Se filtran los resultados para mostrar solo los ICCIDs asignados a distribuidores con el estatus seleccionado.

**Código Modificado:**
- Archivo: `pages/4_📊_Reportes.py`
- Líneas 205-220: Agregado nuevo filtro de estatus de distribuidor
- Líneas 241-265: Modificada lógica de búsqueda para incluir filtrado por estatus de distribuidor

---

## 📊 Casos de Uso

### Caso 1: Obtener ICCIDs de Distribuidores Dados de Baja
1. Ir a **Reportes** → **Consulta Personalizada**
2. Seleccionar **"Estatus del Distribuidor: BAJA"**
3. Hacer clic en **"🔍 Buscar Envíos"**
4. El sistema mostrará todos los ICCIDs asignados a distribuidores con estatus BAJA

### Caso 2: Buscar Distribuidor Específico
1. Ir a **Reportes** → **Por Distribuidor**
2. Escribir el código, nombre o plaza del distribuidor
3. Seleccionar el estatus deseado (ACTIVO, BAJA, etc.)
4. Hacer clic en **"🔍 Buscar Distribuidor"**
5. Seleccionar el distribuidor de la lista de resultados

---

## 🔧 Archivos Modificados

| Archivo | Descripción del Cambio |
| :--- | :--- |
| `pages/4_📊_Reportes.py` | Agregado botón de búsqueda en TAB 3 y nuevo filtro de estatus de distribuidor en TAB 2 |
| `version.py` | Actualizada versión a 1.1.0 |

---

## 📦 Despliegue

**Repositorio:** GitHub - `baitel-sims-nuevo`  
**Branch:** `main`  
**Commits:**
- `3cc7d48`: Mejoras en módulo de Reportes
- `6fbd969`: Actualizar versión a 1.1.0

**Plataforma:** Railway  
**URL de Producción:** https://baitel-sims-nuevo-production.up.railway.app

**Estado del Despliegue:** ✅ Exitoso

---

## ✅ Verificación

Se verificó el correcto funcionamiento de ambas mejoras en el entorno de producción:
- ✅ Botón de búsqueda en "Por Distribuidor" visible y funcional
- ✅ Filtro de "Estatus del Distribuidor" en "Consulta Personalizada" operativo
- ✅ Sistema desplegado correctamente en Railway

---

## 📝 Notas Técnicas

- La lógica de filtrado por estatus de distribuidor se implementa en el lado del cliente (Python) después de obtener los resultados de la base de datos.
- Se realiza una consulta adicional a la tabla `distribuidores` solo cuando se selecciona un estatus específico (diferente de "TODOS").
- El rendimiento no se ve afectado significativamente ya que la consulta de distribuidores es ligera (solo se obtiene el campo `codigo_bt`).

---

**Desarrollado por:** Manus AI  
**Fecha de Release:** 21 de Enero de 2026
