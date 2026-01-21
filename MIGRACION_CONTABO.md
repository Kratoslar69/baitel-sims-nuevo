# 📋 Migración de Baitel SIMs a Contabo VPS

**Fecha:** 27 de diciembre de 2025  
**Sistema:** Baitel SIMs Sistema v1.0.0  
**Origen:** Railway  
**Destino:** Contabo VPS (5.189.174.129)

---

## ✅ Estado Actual de la Migración

### **Sistema Funcionando**
- ✅ **Streamlit** corriendo en puerto 8501 (servicio systemd)
- ✅ **Supabase Cloud** (base de datos en la nube - mantener)
- ✅ **DNS configurado** - admin.baitel.com.mx → 5.189.174.129
- ✅ **Auto-inicio** configurado con systemd
- ✅ **Traefik** corriendo para otras aplicaciones

### **Acceso Actual**
- **URL funcional:** `http://5.189.174.129:8501`
- **URL con dominio:** `http://admin.baitel.com.mx:8501` (funciona)

---

## 🚧 Pendiente: SSL con Dominio

### **Problema Identificado**
El puerto 8443 está **bloqueado por el firewall externo de Contabo**. Los puertos no estándar (diferentes a 80, 443, 22, etc.) están bloqueados por defecto.

### **Solución Recomendada**
Configurar Traefik para que maneje `admin.baitel.com.mx` en el puerto 443 estándar con SSL automático de Let's Encrypt.

---

## 📦 Arquitectura Instalada

### **Servicios Corriendo**

#### **1. Baitel SIMs (Streamlit)**
- **Ubicación:** `/opt/baitel-sims/`
- **Servicio:** `baitel-sims.service` (systemd)
- **Puerto:** 8501
- **Auto-inicio:** ✅ Habilitado
- **Comando:** 
  ```bash
  systemctl status baitel-sims
  systemctl restart baitel-sims
  systemctl stop baitel-sims
  ```

#### **2. Python Environment**
- **Versión:** Python 3.11
- **Virtualenv:** `/opt/baitel-sims/venv/`
- **Dependencias:** Instaladas desde `requirements.txt`

#### **3. Base de Datos**
- **Tipo:** Supabase Cloud (Pro)
- **URL:** `https://xgeqtuwjrkvevthzbuhy.supabase.co`
- **Configuración:** `/opt/baitel-sims/.env`

#### **4. Traefik (Existente)**
- **Versión:** v3.4.0
- **Puertos:** 80, 443
- **SSL:** Let's Encrypt configurado
- **Red:** m4metadryvenet (Docker Swarm overlay)

---

## 📝 Archivos Clave

### **Configuración del Sistema**
```
/opt/baitel-sims/
├── Home.py                          # Archivo principal
├── pages/                           # Páginas de la aplicación
│   ├── 1_📥_Captura_SIMs.py
│   ├── 2_👥_Administrar_Distribuidores.py
│   ├── 3_🔄_Correcciones.py
│   └── 4_📊_Reportes.py
├── utils/                           # Utilidades
│   ├── db.py                        # Conexión a Supabase
│   └── distribuidores_db.py         # Funciones de BD
├── assets/                          # Recursos
│   └── LOGO_BAIT-removebg-preview.png
├── requirements.txt                 # Dependencias Python
├── .env                             # Variables de entorno
└── venv/                            # Entorno virtual Python

/etc/systemd/system/
└── baitel-sims.service              # Servicio systemd
```

### **Contenido del Servicio Systemd**
```ini
[Unit]
Description=Baitel SIMs Sistema - Streamlit Application
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/baitel-sims
Environment="PATH=/opt/baitel-sims/venv/bin"
ExecStart=/opt/baitel-sims/venv/bin/streamlit run Home.py --server.port=8501 --server.address=0.0.0.0 --server.headless=true
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

---

## 🔧 Comandos Útiles

### **Gestión del Servicio**
```bash
# Ver estado
systemctl status baitel-sims

# Reiniciar
systemctl restart baitel-sims

# Ver logs
journalctl -u baitel-sims -f

# Detener
systemctl stop baitel-sims

# Iniciar
systemctl start baitel-sims
```

### **Actualizar el Sistema**
```bash
# 1. Ir al directorio
cd /opt/baitel-sims

# 2. Activar entorno virtual
source venv/bin/activate

# 3. Actualizar código desde GitHub
git pull

# 4. Instalar nuevas dependencias (si hay)
pip install -r requirements.txt

# 5. Reiniciar servicio
systemctl restart baitel-sims
```

### **Ver Logs en Tiempo Real**
```bash
journalctl -u baitel-sims.service -f
```

---

## 🌐 Configuración DNS

### **Registro Actual en Neubox**
```
Tipo: A
Nombre: admin.baitel.com.mx
Valor: 5.189.174.129
TTL: 14400
```

### **Verificar Propagación DNS**
```bash
nslookup admin.baitel.com.mx
```

---

## 🔐 Credenciales y Accesos

### **Supabase Cloud (Pro)**
- **URL:** `https://xgeqtuwjrkvevthzbuhy.supabase.co`
- **Service Role Key:** (almacenada en `/opt/baitel-sims/.env`)
- **Dashboard:** https://supabase.com/dashboard

### **VPS Contabo**
- **IP:** 5.189.174.129
- **Usuario:** root
- **Sistema:** Ubuntu 22.04
- **Acceso SSH:** Configurado con clave SSH

### **GitHub**
- **Repositorio:** https://github.com/Kratoslar69/baitel-sims-nuevo
- **Rama:** main

---

## ⚠️ Problemas Conocidos

### **1. Puerto 8443 Bloqueado**
**Síntoma:** No se puede acceder a `https://admin.baitel.com.mx:8443`  
**Causa:** Firewall externo de Contabo bloquea puertos no estándar  
**Solución:** Usar puerto 443 estándar con Traefik

### **2. Conectividad con Docker Hub**
**Síntoma:** `failed to fetch anonymous token` al hacer `docker build`  
**Causa:** Problema de DNS/conectividad del VPS  
**Solución:** Usar instalación nativa de Python (ya implementada)

---

## 📊 Próximos Pasos

### **Opción A: Mantener Acceso Actual (Temporal)**
- Acceso: `http://admin.baitel.com.mx:8501`
- Sin SSL
- Funcional pero no ideal

### **Opción B: Configurar SSL con Traefik (Recomendado)**
1. Crear configuración dinámica de Traefik
2. Configurar proxy a puerto 8501
3. SSL automático con Let's Encrypt
4. Acceso: `https://admin.baitel.com.mx` (puerto 443)

---

## 💰 Costos

### **Antes (Railway)**
- **Costo mensual:** ~$20-30 USD (variable según uso)
- **Límites:** Según plan

### **Después (Contabo VPS)**
- **Costo VPS:** ~$5-15 USD/mes (fijo)
- **Supabase Pro:** $25 USD/mes
- **Total:** ~$30-40 USD/mes (fijo y predecible)

---

## 📞 Soporte

### **Comandos de Diagnóstico**
```bash
# Ver si Streamlit está corriendo
systemctl status baitel-sims

# Ver logs de errores
journalctl -u baitel-sims -n 100 --no-pager

# Verificar puerto 8501
netstat -tuln | grep 8501

# Probar conectividad a Supabase
curl -I https://xgeqtuwjrkvevthzbuhy.supabase.co
```

### **Reinicio Completo**
```bash
systemctl restart baitel-sims
```

---

## ✅ Checklist de Migración

- [x] Clonar repositorio en VPS
- [x] Instalar Python 3.11 y dependencias
- [x] Configurar variables de entorno (.env)
- [x] Crear servicio systemd
- [x] Habilitar auto-inicio
- [x] Configurar DNS (admin.baitel.com.mx)
- [x] Verificar funcionamiento básico
- [ ] Configurar SSL con Traefik
- [ ] Probar todas las funcionalidades
- [ ] Apagar Railway (cuando esté 100% estable)

---

**Documento creado:** 27/12/2025  
**Última actualización:** 27/12/2025  
**Estado:** Migración parcial completada - Pendiente SSL
