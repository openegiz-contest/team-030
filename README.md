# <Team name>: a digital mine on OpenEgiz

> Team Repository of the contest “Digital Mine on OpenEgiz”. **Replace the contents of this file with the instructions for your Submission.** The AI Jury runs the Submission strictly by these instructions, from scratch, in the Judge Environment. Accepted languages: English, Kazakh, Russian.

# Kachar Mine Digital Twin

Digital Mine on OpenEgiz байқауына арналған Қашар карьерінің цифрлық егізі.

## Жоба туралы

Жоба карьердегі экскаваторлар мен самосвалдардың есептік өнімділігін модельдейді.

Барлық өндірістік параметрлер демонстрациялық болжамдар болып табылады.

## Технологиялар

- Python
- MQTT
- Eclipse Ditto
- InfluxDB
- Grafana
- Docker

## Іске қосу

Docker Desktop, Docker Compose, Make, Python 3 және python3-venv қажет.

```bash
make up
bash team/kachar-mine/run.sh
```

## Нәтижелер

- Қазіргі өнімділік: 800 т/сағ
- What-if: 3 экскаватор — 1080 т/сағ
- Есептік өсім: 35%

## Визуализация

Grafana: http://localhost:3000

Dashboard: Kachar Mine Digital Twin

## Жоба файлдары

- `team/kachar-mine/simulator.py` — өнімділікті есептеу
- `team/kachar-mine/mqtt_simulator.py` — MQTT арқылы дерек жіберу
- `team/kachar-mine/setup_twins.py` — Digital Twin жасау
- `team/kachar-mine/twins.json` — цифрлық егіздің бастапқы деректері
- `team/kachar-mine/run.sh` — іске қосу
- `SUBMISSION.md` — жоба сипаттамасы
- `presentation.pdf` — презентация

## Kachar Mine Interactive Dashboard

The Kachar Mine Digital Twin includes an interactive web dashboard.

### Features
- Animated mine equipment and haul trucks
- Excavator and truck fleet controls
- Maintenance simulation and equipment status
- Production chart and pause/resume controls
- Eclipse Ditto API integration
- Production scenario comparison: 800 t/h vs 1080 t/h (+35%)

### Start the dashboard

First, start the OpenEgiz Docker platform using the deployment instructions.

Then run:

```bash
bash team/kachar-mine/web/start.sh

Open:

http://localhost:8766/

The dashboard reads simulated production data from Eclipse Ditto.
The animated equipment and what-if controls are browser-side simulations.

The local file `deploy/compose/.env` must contain `DITTO_PASSWORD`.
Do not commit passwords or `.env` files to GitHub.
