from fpdf import FPDF

# Create a PDF class


class PDF(FPDF):
    def header(self):
        self.set_font("Roboto", "B", 14)
        self.cell(
            0, 10, "Docker Learning Plan (Beginner to Intermediate)", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, title, ln=True, align="L")
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 8, body)
        self.ln()


# Initialize PDF
pdf = PDF()
pdf.add_page()

# Add content
with open("docker.txt", "r") as file:
    content = file.read()


sections = content.split('---')
for section in sections:
    lines = section.strip().split('\n')
    if not lines:
        continue
    title = lines[0] if lines else "Section"
    body = "\n".join(lines[1:])
    pdf.chapter_title(title)
    pdf.chapter_body(body)

# Save PDF (fpdf2 supports Unicode by default)
pdf_path = "./Docker_Learning_Plan.pdf"
pdf.output(pdf_path)
