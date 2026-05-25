#!/usr/bin/env bash
set -euo pipefail

APP_DIR="/var/www/askharekrishna-platform/backend"
SERVICE_NAME="gunicorn-askharekrishna.service"
VENV_DIR="$APP_DIR/venv"
PYTHON_BIN="$VENV_DIR/bin/python"

cd "$APP_DIR"

echo ">>> Pulling latest backend code"
git pull --ff-only origin master

echo ">>> Ensuring virtual environment"
if [[ ! -d "$VENV_DIR" ]]; then
  python3 -m venv "$VENV_DIR"
fi

echo ">>> Installing backend dependencies"
"$PYTHON_BIN" -m pip install --upgrade pip
"$PYTHON_BIN" -m pip install -r requirements.txt

echo ">>> Applying migrations"
"$PYTHON_BIN" manage.py migrate --noinput

echo ">>> Collecting static files"
"$PYTHON_BIN" manage.py collectstatic --noinput

echo ">>> Restarting backend service"
sudo systemctl restart "$SERVICE_NAME"
sudo systemctl --no-pager --full status "$SERVICE_NAME" | head -n 40

echo ">>> Backend deployment successful"
