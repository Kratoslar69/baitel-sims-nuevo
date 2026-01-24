# 🚀 Baitel SIMs - Entorno de Desarrollo v1.2.0

**Branch:** `dev-ventas`  
**Estado:** En desarrollo  
**Propósito:** Implementar módulo de ventas sin afectar producción

---

## ⚠️ IMPORTANTE

**Este es el entorno de DESARROLLO.**

- ❌ NO usar en producción
- ❌ NO contiene datos reales de producción
- ✅ Usar solo para desarrollo y pruebas

---

## 🎯 Objetivo de esta Versión

Implementar módulo completo de ventas con:
- Carga de archivos de ventas (Excel)
- Dashboards de ventas por tipo y estatus
- Sistema de warnings automáticos
- Reportes exportables
- Análisis de inventario

---

## 🔧 Configuración del Entorno

### **Variables de Entorno:**

```bash
SUPABASE_URL=https://tskihgbxsxkwvfmoiffs.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### **Base de Datos:**

**Tablas:**
- `distribuidores` (clonada de producción)
- `envios` (clonada de producción)
- `ventas` (nueva tabla para este módulo)

---

## 🚀 Ejecutar Localmente

```bash
# Clonar repositorio
git clone https://github.com/Kratoslar69/baitel-sims-nuevo.git
cd baitel-sims-nuevo

# Cambiar a branch de desarrollo
git checkout dev-ventas

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
export SUPABASE_URL="https://tskihgbxsxkwvfmoiffs.supabase.co"
export SUPABASE_KEY="tu_key_aqui"

# Ejecutar aplicación
streamlit run Home.py
```

---

## 📊 Estructura de la Tabla de Ventas

```sql
CREATE TABLE ventas (
    id UUID PRIMARY KEY,
    iccid VARCHAR(50) NOT NULL,
    asignacion VARCHAR(255),
    distribuidor VARCHAR(255),
    estatus_socio VARCHAR(20),
    msisdn BIGINT,
    estatus_operacion VARCHAR(20),
    fecha_activacion TIMESTAMP,
    fecha_port_in TIMESTAMP,
    tipo_venta VARCHAR(50),
    fecha_port_out TIMESTAMP,
    consumo_voz NUMERIC,
    consumo_datos NUMERIC,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(iccid, fecha_activacion)
);
```

---

## 🔄 Flujo de Migración a Producción

Cuando el desarrollo esté completo y aprobado:

1. Crear tabla `ventas` en Supabase Producción
2. Merge `dev-ventas` → `main`
3. Railway Producción autodespliega
4. Sistema completo en producción

---

## 📝 Cambios en esta Versión

### **Nuevas Páginas:**
- `pages/5_📊_Ventas.py` - Módulo de ventas completo

### **Nuevas Utilidades:**
- `utils/ventas_db.py` - CRUD para tabla de ventas
- `utils/ventas_analytics.py` - Análisis y dashboards
- `utils/ventas_warnings.py` - Sistema de alertas

### **Archivos Modificados:**
- `version.py` - Actualizado a v1.2.0
- `requirements.txt` - Dependencias adicionales (si aplica)

---

## 🛡️ Seguridad

- Las credenciales de desarrollo NO deben usarse en producción
- Los datos en Supabase Dev son de prueba
- No compartir las credenciales públicamente

---

## 📞 Soporte

Para dudas o problemas con el desarrollo, contactar al equipo de desarrollo.

---

**Desarrollado por:** Manus AI  
**Fecha de inicio:** 21 de Enero de 2026  
**Estado:** 🔄 En desarrollo activo
