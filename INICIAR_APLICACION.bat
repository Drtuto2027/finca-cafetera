@echo off
chcp 65001 >nul
echo ========================================
echo   INICIANDO APLICACION DJANGO
echo   Sistema de Gestion Cafetera
echo ========================================
echo.
echo Tu IP local es:
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /C:"IPv4"') do echo %%a
echo.
pause

REM Verificar si Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado o no esta en el PATH
    pause
    exit /b 1
)

echo Verificando dependencias...
python -m pip install -r requirements.txt --quiet

echo.
echo Iniciando servidor Django...
echo.
echo La aplicacion estara disponible en:
echo   http://127.0.0.1:8000 (desde este PC)
echo   http://10.0.0.50:8000 (desde el movil en la misma red)
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

python manage.py runserver 0.0.0.0:8000

pause



