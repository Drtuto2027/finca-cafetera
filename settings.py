"""
CONFIGURACIÓN CORREGIDA - Sin errores de importación
"""

from pathlib import Path
import os

# Intentar cargar .env si python-dotenv está instalado
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-clave-super-secreta-cafetera-2024-mysql-final')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Permitir acceso desde la red local
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1,*').split(',')

# APPS EN ORDEN CORRECTO
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Apps del sistema - ORDEN IMPORTANTE
    'core',          # App principal con vistas y templates
    'usuarios',      # Primero porque define AUTH_USER_MODEL
    'produccion',    # Segundo - modelos base
    'inventario',    # Tercero - depende de produccion
    'pagos',         # Cuarto - depende de produccion
    'beneficio',     # Quinto - proceso de beneficio del café
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

# Configuración mínima de templates requerida por Django admin
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuración de Base de Datos MySQL con PyMySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'finca_cafetera_db',
        'USER': 'root',
        'PASSWORD': '',  # Sin contraseña
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    }
}

# Configurar PyMySQL como driver de MySQL
import pymysql
pymysql.install_as_MySQLdb()

AUTH_USER_MODEL = 'usuarios.Usuario'

LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = False  # Deshabilitado para MySQL - MySQL no maneja bien timezones nativamente

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de Email para Recuperación de Contraseña
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Para desarrollo
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Para producción
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'tu-correo@gmail.com'
# EMAIL_HOST_PASSWORD = 'tu-contraseña-app'
# DEFAULT_FROM_EMAIL = 'noreply@fincacafetera.com'

