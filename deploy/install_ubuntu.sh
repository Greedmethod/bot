#!/usr/bin/env bash
set -euo pipefail

APP_USER="highrisebot"
APP_DIR="/opt/highrise-bot"
SERVICE_FILE="highrise-bot.service"

if [[ "${EUID}" -ne 0 ]]; then
  echo "Run this installer as root: sudo bash deploy/install_ubuntu.sh"
  exit 1
fi

apt update
apt install -y python3 python3-venv python3-pip git

if ! id -u "${APP_USER}" >/dev/null 2>&1; then
  useradd --system --create-home --shell /usr/sbin/nologin "${APP_USER}"
fi

mkdir -p "${APP_DIR}"
cp -a . "${APP_DIR}"
chown -R "${APP_USER}:${APP_USER}" "${APP_DIR}"

sudo -u "${APP_USER}" python3 -m venv "${APP_DIR}/.venv"
sudo -u "${APP_USER}" "${APP_DIR}/.venv/bin/pip" install --upgrade pip setuptools wheel
sudo -u "${APP_USER}" "${APP_DIR}/.venv/bin/pip" install -r "${APP_DIR}/requirements.txt"

install -m 644 "${APP_DIR}/deploy/${SERVICE_FILE}" "/etc/systemd/system/${SERVICE_FILE}"
systemctl daemon-reload
systemctl enable "${SERVICE_FILE}"

echo "Done. Edit ${APP_DIR}/config/config.py, then run:"
echo "  systemctl start ${SERVICE_FILE}"
echo "  systemctl status ${SERVICE_FILE}"
