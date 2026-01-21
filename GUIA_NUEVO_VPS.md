> Este documento asume que ya has contratado un nuevo VPS y tienes acceso `root` a través de SSH.

# Guía de Preparación y Migración a Nuevo VPS

**Fecha:** 27 de Diciembre de 2025

## 1. Recomendaciones de Proveedor y Servidor

Para evitar los problemas de recursos y estabilidad encontrados en Contabo, se recomienda optar por proveedores enfocados en desarrolladores con infraestructura de alta calidad.

| Proveedor | Ventajas | Plan Recomendado (Ejemplo) |
| :--- | :--- | :--- |
| **DigitalOcean** | Muy fácil de usar, excelente documentación, red confiable. | Droplet 4GB RAM / 2 vCPU |
| **Linode** | Rendimiento sólido, precios competitivos, buen soporte. | Linode 4GB |
| **Vultr** | Amplia presencia global, opciones de alto rendimiento. | High Frequency 4GB RAM |
| **Hetzner** | Excelente relación precio/rendimiento (si no te importa la ubicación en Europa). | Cloud CPX31 (4 vCPU / 8 GB RAM) |

**Especificaciones Mínimas Recomendadas:**
- **RAM:** 4 GB (8 GB es ideal para no tener problemas a futuro)
- **vCPUs:** 2 núcleos
- **Almacenamiento:** 80 GB SSD NVMe
- **Sistema Operativo:** Ubuntu 22.04 LTS

## 2. Configuración Inicial del Servidor (Post-Formateo)

Estos comandos deben ejecutarse como usuario `root` en el nuevo servidor.

### Paso 2.1: Actualización del Sistema

```bash
apt update && apt upgrade -y
```

### Paso 2.2: Instalación de Docker y Docker Compose

El script oficial de Docker simplifica la instalación.

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

### Paso 2.3: Inicialización de Docker Swarm

Esto prepara el entorno para desplegar tus stacks de servicios.

```bash
docker swarm init
```

### Paso 2.4: (Opcional pero Recomendado) Crear Usuario No-Root

Para mejorar la seguridad, no es recomendable operar todo como `root`.

```bash
# Reemplaza 'usuario' con tu nombre de usuario deseado
adduser usuario

# Añadir el nuevo usuario al grupo 'sudo' y 'docker'
usermod -aG sudo usuario
usermod -aG docker usuario

# Cambiar al nuevo usuario
su - usuario
```

## 3. Despliegue de Aplicaciones

Una vez que el servidor esté preparado, puedes proceder a desplegar tus aplicaciones Docker Swarm. Asegúrate de tener tus archivos `docker-compose.yml` listos.

```bash
# Ejemplo de despliegue de un stack llamado 'monitoring'
docker stack deploy -c docker-compose-monitoring.yml monitoring
```

## 4. Migración de Baitel SIMs (Fase Futura)

Cuando decidas migrar el sistema Baitel SIMs del entorno de Railway al nuevo VPS, los pasos serán:

1.  Clonar el repositorio de GitHub en el nuevo servidor.
2.  Construir la imagen de Docker.
3.  Desplegarla como un servicio dentro del Swarm, exponiendo el puerto `8501`.
4.  Configurar un proxy inverso (como Traefik, que ya usas) para asignar el dominio `admin.baitel.com.mx` y gestionar el SSL.

> **Nota:** Se proporcionará un plan detallado para esta fase cuando llegue el momento.
