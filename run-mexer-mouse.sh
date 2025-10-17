#!/bin/bash
# Script para criar venv, ativar e rodar o mexer-mouse.py no macOS

# Caminho da pasta do projeto
PROJECT_DIR="/Users/pedroeuropeu/desenvolvimento/UNICESUMAR/python-stubs"

# Caminho completo do script Python
SCRIPT="$PROJECT_DIR/mexer-mouse.py"

# Entra na pasta
cd "$PROJECT_DIR" || { echo "❌ Erro: não foi possível acessar $PROJECT_DIR"; exit 1; }

# Cria o ambiente virtual, se não existir
if [ ! -d ".venv" ]; then
  echo "📦 Criando ambiente virtual..."
  python3 -m venv .venv
fi

# Ativa o ambiente virtual
echo "🚀 Ativando ambiente virtual..."
source .venv/bin/activate

# Garante que as dependências necessárias estejam instaladas
echo "📚 Instalando dependências..."
pip install --upgrade pip
pip install pyautogui keyboard
pip install pyautogui pynput

# Executa o script
echo "🖱️ Iniciando o script de movimento do mouse..."
python3 "$SCRIPT"

# (opcional) desativa o ambiente virtual após encerrar
deactivate
echo "✅ Execução finalizada."
