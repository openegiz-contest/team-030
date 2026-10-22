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
