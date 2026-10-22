#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/../.."

echo "1. Python ортасын дайындау..."
python3 -m venv team/kachar-mine/.venv
team/kachar-mine/.venv/bin/python -m pip install -r team/kachar-mine/requirements.txt

echo "2. Қашар карьерінің Digital Twin моделін жасау..."
set -a
source deploy/compose/.env
set +a

python3 team/kachar-mine/setup_twins.py

echo "3. MQTT арқылы мәлімет жіберу..."
team/kachar-mine/.venv/bin/python team/kachar-mine/mqtt_simulator.py

echo "Қашар карьерінің моделі іске қосылды!"
