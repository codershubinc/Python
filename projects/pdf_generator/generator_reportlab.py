from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors

# Read content from docker.txt
with open("docker.txt", "r", encoding="utf-8") as file:
    content = file.read()

sections = content.split('---')

# Create PDF
doc = SimpleDocTemplate(
    "Docker_Learning_Plan_reportlab.pdf",
    pagesize=A4,
    rightMargin=40, leftMargin=40, topMargin=60, bottomMargin=40
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='SectionTitle', fontSize=14, leading=18, alignment=TA_LEFT,
           spaceAfter=8, textColor=colors.HexColor('#1e1e1e'), fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='SectionBody', fontSize=11, leading=15, alignment=TA_LEFT,
           spaceAfter=12, textColor=colors.HexColor('#323232'), fontName='Helvetica'))

story = []

# Add a main title
story.append(
    Paragraph("Docker Learning Plan (Beginner to Intermediate)", styles['Title']))
story.append(Spacer(1, 16))

for section in sections:
    lines = section.strip().split('\n')
    if not lines or not lines[0].strip():
        continue
    title = lines[0]
    body = "\n".join(lines[1:])
    story.append(Paragraph(title, styles['SectionTitle']))
    story.append(Paragraph(body, styles['SectionBody']))
    story.append(Spacer(1, 8))

# Build PDF
doc.build(story)
