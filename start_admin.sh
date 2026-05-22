#!/bin/bash
# ======================================================================
# NETAD Administrator Quick Start - Linux/Mac
# ======================================================================

set -e  # Exit on error

echo ""
echo "======================================================================"
echo "  NETAD Finals - System Administrator Setup"
echo "======================================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3.11+ from https://www.python.org/"
    exit 1
fi

echo "[OK] Python 3 is installed: $(python3 --version)"
echo ""

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "[WARNING] .env file not found"
    echo "Creating .env from .env.example..."
    if [ -f ".env.example" ]; then
        cp ".env.example" ".env"
        echo "[OK] .env created from template"
    else
        echo "[ERROR] .env.example not found"
        exit 1
    fi
fi

echo ""
echo "======================================================================"
echo "  Step 1: Installing Dependencies"
echo "======================================================================"
echo ""

pip3 install -q -r requirements.txt || {
    echo "[ERROR] Failed to install dependencies"
    exit 1
}

echo "[OK] Dependencies installed"
echo ""

echo "======================================================================"
echo "  Step 2: Setting Up Administrator Account"
echo "======================================================================"
echo ""

python3 admin_setup.py || {
    echo "[ERROR] Admin setup failed"
    echo ""
    echo "Trying emergency reset..."
    python3 admin_reset.py || {
        echo "[ERROR] Admin reset also failed"
        exit 1
    }
}

echo ""
echo "======================================================================"
echo "  Step 3: Starting Application"
echo "======================================================================"
echo ""

python3 app.py
