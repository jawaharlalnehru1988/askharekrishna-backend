#!/usr/bin/env bash
set -euo pipefail

APP_DIR="/var/www/askharekrishna-platform/backend"
SERVICE_NAME="gunicorn-askharekrishna.service"

cd "$APP_DIR"

echo ">>> Pulling latest backend code"
git pull --ff-only origin master

if [[ -d "venv" ]]; then
  # shellcheck disable=SC1091
  source venv/bin/activate
fi

echo ">>> Installing backend dependencies"
python3 -m pip install --upgrade pip
pip install -r requirements.txt

echo ">>> Applying migrations"
python3 manage.py migrate --noinput

echo ">>> Collecting static files"
python3 manage.py collectstatic --noinput

echo ">>> Restarting backend service"
sudo systemctl restart "$SERVICE_NAME"
sudo systemctl --no-pager --full status "$SERVICE_NAME" | head -n 40

echo ">>> Backend deployment successful"
