# 🚀 GUÍA DE INICIO - Sistema de Gestión Cafetera

## 📁 Archivos Principales para Iniciar la Aplicación

### Archivos Esenciales:
1. **`manage.py`** - Archivo principal de Django para ejecutar comandos
2. **`settings.py`** - Configuración del proyecto Django
3. **`urls.py`** - Configuración de rutas/URLs de la aplicación
4. **`requirements.txt`** - Dependencias del proyecto

## 🎯 Formas de Iniciar la Aplicación

### Opción 1: Usando el Script de Inicio (Recomendado)
- **Windows (PowerShell)**: Doble clic en `INICIAR_APLICACION.ps1`
- **Windows (CMD)**: Doble clic en `INICIAR_APLICACION.bat`

### Opción 2: Desde la Terminal/CMD
```bash
# 1. Navegar a la carpeta del proyecto
cd "C:\Users\USUARIO\OneDrive - Politécnico Grancolombiano\Escritorio\CASTAÑEDA\desarrollo de software1"

# 2. Instalar dependencias (si es la primera vez)
pip install -r requirements.txt

# 3. Iniciar el servidor
python manage.py runserver
```

### Opción 3: Desde PowerShell
```powershell
# 1. Navegar a la carpeta del proyecto
cd "C:\Users\USUARIO\OneDrive - Politécnico Grancolombiano\Escritorio\CASTAÑEDA\desarrollo de software1"

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Iniciar el servidor
python manage.py runserver
```

## 🌐 Acceso a la Aplicación

Una vez iniciado el servidor, la aplicación estará disponible en:
- **URL Principal**: http://127.0.0.1:8000/admin/
- **Puerto**: 8000 (por defecto)

## 📋 Comandos Útiles

### Crear un superusuario (primera vez)
```bash
python manage.py createsuperuser
```

### Aplicar migraciones de base de datos
```bash
python manage.py migrate
```

### Verificar estado de la base de datos
```bash
python verificar_db.py
```

## ⚙️ Requisitos Previos

1. **Python 3.8+** instalado
2. **MySQL** instalado y corriendo
3. **Base de datos** `finca_cafetera_db` creada en MySQL
4. **Dependencias** instaladas desde `requirements.txt`

## 📦 Dependencias del Proyecto

- Django==4.2.7
- python-dotenv==1.0.0
- PyMySQL==1.1.2
- cryptography==46.0.2

## 🗂️ Estructura del Proyecto

```
desarrollo de software1/
├── manage.py              ← ARCHIVO PRINCIPAL PARA INICIAR
├── settings.py            ← Configuración del proyecto
├── urls.py                ← Rutas de la aplicación
├── requirements.txt       ← Dependencias
├── INICIAR_APLICACION.bat ← Script de inicio (Windows CMD)
├── INICIAR_APLICACION.ps1 ← Script de inicio (PowerShell)
├── usuarios/              ← App de usuarios
├── produccion/            ← App de producción
├── inventario/            ← App de inventario
├── pagos/                 ← App de pagos
└── beneficio/             ← App de beneficio
```

## ❓ Problemas Comunes

### Error: "Python no reconocido"
- Asegúrate de tener Python instalado
- Verifica que Python esté en el PATH del sistema

### Error: "No module named 'django'"
- Ejecuta: `pip install -r requirements.txt`

### Error de conexión a MySQL
- Verifica que MySQL esté corriendo
- Verifica la configuración en `settings.py`
- Asegúrate de que la base de datos `finca_cafetera_db` exista

---

**¡Listo para iniciar!** 🎉



