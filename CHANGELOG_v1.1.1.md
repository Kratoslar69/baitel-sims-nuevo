# Changelog v1.1.1 - "Claridad y Correcciones"

**Fecha de Lanzamiento**: 01 de Febrero de 2026  
**Tipo de Versión**: Patch (Corrección y Refactorización)

---

## 📋 Resumen

Versión enfocada en mejorar la claridad del código y la estructura de la base de datos mediante el renombrado de columnas ambiguas. Se corrigió el filtro por estatus de distribuidor en el módulo de Reportes y se optimizaron las consultas SQL.

---

## ✨ Cambios Principales

### 🔄 Refactorización de Base de Datos

#### Renombrado de Columnas
Para evitar confusiones y mejorar la legibilidad del código:

**Tabla `distribuidores`:**
- `estatus` → `estatus_distribuidor`
- **Valores**: ACTIVO, BAJA, SUSPENDIDO

**Tabla `envios`:**
- `estatus` → `estatus_envio`
- **Valores**: ACTIVO, REASIGNADO, CANCELADO

**Impacto:**
- ✅ Mayor claridad en el código
- ✅ Evita ambigüedades al trabajar con JOINs
- ✅ Facilita el mantenimiento futuro
- ✅ Mejora la documentación implícita del código

---

### 🐛 Correcciones de Bugs

#### 1. Filtro por Estatus de Distribuidor en Reportes
**Problema:** El módulo de Reportes no filtraba correctamente por estatus de distribuidor.

**Solución Implementada:**
- Agregado parámetro `codigos_bt_validos` en `buscar_envios()`
- Implementado filtro SQL usando operador `IN` para mayor eficiencia
- Optimizada la consulta para obtener primero los códigos BT válidos

**Código Clave:**
```python
# Obtener distribuidores con el estatus seleccionado
dist_filtrados = supabase.table('distribuidores')\
    .select('codigo_bt')\
    .eq('estatus_distribuidor', estatus_dist_buscar)\
    .execute()

codigos_bt_filtrados = [d['codigo_bt'] for d in dist_filtrados.data]

# Filtrar envíos usando SQL IN
resultados = buscar_envios(
    ...
    codigos_bt_validos=codigos_bt_filtrados
)
```

**Resultado:**
- ✅ Filtro por "ACTIVO" funciona correctamente
- ✅ Filtro por "BAJA" funciona correctamente
- ✅ Filtro por "SUSPENDIDO" funciona correctamente
- ✅ Consultas más eficientes (filtro en SQL vs post-procesamiento)

---

## 📁 Archivos Modificados

### Utilidades
- `utils/distribuidores_db.py` - Actualizado para usar `estatus_distribuidor`
- `utils/envios_db.py` - Actualizado para usar `estatus_envio` y agregado parámetro `codigos_bt_validos`

### Páginas del Sistema
- `Home.py` - Consultas actualizadas
- `pages/1_📥_Captura_SIMs.py` - Referencias actualizadas
- `pages/2_👥_Administrar_Distribuidores.py` - CRUD actualizado
- `pages/3_🔄_Correcciones.py` - Módulo de correcciones actualizado
- `pages/4_📊_Reportes.py` - Filtros corregidos y optimizados

### Configuración
- `version.py` - Actualizado a v1.1.1

---

## 🔧 Cambios Técnicos

### Base de Datos
```sql
-- Comandos ejecutados en Supabase
ALTER TABLE distribuidores RENAME COLUMN estatus TO estatus_distribuidor;
ALTER TABLE envios RENAME COLUMN estatus TO estatus_envio;
```

### Función `buscar_envios()` Mejorada
```python
def buscar_envios(
    iccid: Optional[str] = None,
    codigo_bt: Optional[str] = None,
    fecha_desde: Optional[date] = None,
    fecha_hasta: Optional[date] = None,
    estatus: Optional[str] = None,
    limit: int = 100,
    codigos_bt_validos: Optional[List[str]] = None  # NUEVO
) -> List[Dict]:
    # ...
    if codigos_bt_validos is not None:
        query = query.in_('codigo_bt', codigos_bt_validos)
    # ...
```

---

## 📊 Estadísticas de Datos Verificadas

Durante las pruebas se confirmó:
- **366 distribuidores activos** con 104,025 SIMs asignadas
- **Distribuidores con estatus BAJA** que tienen envíos históricos:
  - BT025-TAPACHULA: 2,650 envíos
  - BT296-MORELIA 3: 1,660 envíos
  - BT108-CACOCOYAGUA: 770 envíos
  - Y más...

**Total**: Más de 8,000 envíos históricos de distribuidores dados de baja

---

## ⚠️ Notas Importantes

### Compatibilidad
- ⚠️ **Breaking Change**: Este cambio modifica la estructura de la base de datos
- ⚠️ Cualquier código externo que acceda directamente a las tablas debe actualizarse
- ✅ La migración se realizó usando `ALTER TABLE` sin pérdida de datos

### Procedimiento de Despliegue
1. ✅ Código actualizado y pusheado a GitHub
2. ✅ Columnas renombradas en Supabase
3. ✅ Railway desplegó automáticamente
4. ✅ Sistema verificado en producción

---

## 🎯 Lecciones Aprendidas

### Sobre el Filtro de Reportes
El análisis reveló que el filtro funcionaba correctamente, pero los distribuidores dados de BAJA tienen envíos con fechas antiguas (2024-2025). Al buscar con rangos de fechas recientes (2026), no aparecían resultados.

**Recomendación para usuarios:**
- Al buscar envíos de distribuidores BAJA, usar rangos de fechas amplios
- Considerar que distribuidores dados de baja tienen envíos históricos

---

## 🚀 Próximos Pasos

### v1.2.0 (Planificada)
- Módulo de Ventas y Comisiones
- Dashboard de análisis de ventas
- Cálculo automático de comisiones
- Reportes de rendimiento por distribuidor

---

## 📝 Commits Incluidos

- `754a6c8` - Fix: Corrección del filtro por estatus de distribuidor en Reportes
- `fb23e27` - Refactor: Renombrar columnas de estatus para mayor claridad

---

## 🔗 Enlaces

- **Repositorio**: https://github.com/Kratoslar69/baitel-sims-nuevo
- **Producción**: https://baitel-sims-nuevo-production-43aa.up.railway.app
- **Base de Datos**: Supabase (proyecto: xgeqtuwjrkvevthzbuhy)

---

**Desarrollado por**: Manus AI  
**Fecha de Documentación**: 01/02/2026  
**Versión**: v1.1.1
