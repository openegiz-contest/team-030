from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

pdfmetrics.registerFont(
    TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
)

W, H = 960, 540
c = canvas.Canvas("presentation.pdf", pagesize=(W, H))

NAVY = HexColor("#101E33")
WHITE = HexColor("#FFFFFF")
CYAN = HexColor("#42D7DB")
MUTED = HexColor("#B8C7D9")

def text(x, y, value, size=20, color=WHITE):
    c.setFont("DejaVu", size)
    c.setFillColor(color)
    c.drawString(x, y, value)

def slide(title, lines, number):
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(CYAN)
    c.rect(55, 455, 7, 42, fill=1, stroke=0)
    text(80, 466, title, 28)
    for i, line in enumerate(lines):
        text(65, 385 - i * 55, line, 19)
    text(65, 35, "Kachar Mine Digital Twin | OpenEgiz", 12, MUTED)
    text(875, 35, f"{number}/6", 12, MUTED)
    c.showPage()

slide("Kachar Mine Digital Twin", [
    "Digital Mine on OpenEgiz",
    "Қашар темір кені карьерінің цифрлық моделі",
    "Мақсат: өндіріс өнімділігін жоспарлау",
    "GitHub: ernarsajdullin05-wq"
], 1)

slide("Өндірістік мәселе", [
    "Карьерде техника мүмкіндіктерін үйлестіру маңызды.",
    "Экскаватор мен самосвал өнімділігі әртүрлі болуы мүмкін.",
    "Жүйе өндірістің шектеуші факторын есептейді.",
    "Модель нақты деректерге емес, болжамдарға негізделген."
], 2)

slide("Жүйенің архитектурасы", [
    "Python — өндірістік есептеу",
    "MQTT — телеметрия жіберу",
    "Eclipse Ditto — цифрлық егіз",
    "InfluxDB — көрсеткіштерді сақтау",
    "Grafana — мониторинг және What-if"
], 3)

slide("Өндіріс моделі", [
    "4 самосвал × 90 тонна × 3 рейс/сағ = 1080 т/сағ",
    "2 экскаватор × 400 т/сағ = 800 т/сағ",
    "Жүйе өнімділігі: min(1080, 800) = 800 т/сағ",
    "Барлық параметрлер — демонстрациялық болжамдар."
], 4)

slide("Интерактивті What-if", [
    "Grafana мәзірінде экскаватор санын таңдауға болады.",
    "1 экскаватор: 400 т/сағ",
    "2 экскаватор: 800 т/сағ",
    "3 немесе 4 экскаватор: 1080 т/сағ",
    "2-ден 3-ке ауысқанда есептік өсім: +35%"
], 5)

slide("Нәтиже және шектеулер", [
    "Ditto + MQTT + InfluxDB + Grafana байланысы іске қосылды.",
    "What-if Grafana ішінде код өзгертпей есептеледі.",
    "Grafana таңдауы Ditto күйін әзірге өзгертпейді.",
    "Нақты өндірістік деректер және бос тұру есебі жоқ.",
    "Репозиторий: github.com/openegiz-contest/team-030"
], 6)

c.save()
print("presentation.pdf жасалды!")
