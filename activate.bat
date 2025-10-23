@echo off
setlocal

REM === Caminho do ambiente virtual ===
set VENV_DIR=.\speech_env

echo ============================================
echo Audio-to-Text Whisper Runner
echo ============================================

REM === Cria o ambiente se não existir ===
if not exist "%VENV_DIR%\Scripts\activate" (
    echo.
    echo 🚀 Criando ambiente virtual...
    python -m venv "%VENV_DIR%"
)

REM === Ativa o ambiente ===
call "%VENV_DIR%\Scripts\activate"

REM === Instala dependências ===
echo.
echo Instalando dependências (isso pode levar alguns minutos)...
python.exe -m pip install --upgrade pip
pip install -r requirements.txt

REM === Executa o script principal ===
echo.
echo Rodando transcrição com Whisper...
python batch_audio_to_text_whisper.py

REM === Fim ===
echo.
echo ✅ Finalizado.
pause
