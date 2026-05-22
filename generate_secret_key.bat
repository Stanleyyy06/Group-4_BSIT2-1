@echo off
REM generate_secret_key.bat - Generate a secure SECRET_KEY for production (Windows)

echo.
echo 🔐 Generating secure SECRET_KEY...
echo.

REM Python method (recommended)
for /f "delims=" %%i in ('python -c "import secrets; print(secrets.token_hex(32))"') do set SECRET_KEY=%%i

echo.
echo ✅ Your SECRET_KEY (64 characters):
echo.
echo SECRET_KEY=%SECRET_KEY%
echo.
echo 📋 Copy this to your .env or Railway variables
echo.
