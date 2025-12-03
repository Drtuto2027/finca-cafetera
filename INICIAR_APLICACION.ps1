# Script para iniciar la aplicación Django
# Sistema de Gestión Cafetera

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  INICIANDO APLICACION DJANGO" -ForegroundColor Cyan
Write-Host "  Sistema de Gestión Cafetera" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ ERROR: Python no está instalado o no está en el PATH" -ForegroundColor Red
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host "Verificando dependencias..." -ForegroundColor Yellow
python -m pip install -r requirements.txt --quiet

Write-Host ""
Write-Host "Iniciando servidor Django..." -ForegroundColor Green
Write-Host ""
Write-Host "La aplicación estará disponible en:" -ForegroundColor Cyan
Write-Host "  http://127.0.0.1:8000/admin/" -ForegroundColor Yellow
Write-Host ""
Write-Host "Presiona Ctrl+C para detener el servidor" -ForegroundColor Gray
Write-Host ""

python manage.py runserver



