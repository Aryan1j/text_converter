from PIL import Image, ImageDraw, ImageFont
import textwrap
from docx import Document
from docx.shared import Pt
from fpdf import FPDF

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

width, height = 1200, 700
background_color = "#FFF9F0"
text_color = "#2E2E2E"
font_size = 40
line_spacing = 25

try:
    font = ImageFont.truetype("arial.ttf", font_size)
except:
    print("⚠️ Using fallback font — install 'arial.ttf' for better results.")
    font = ImageFont.load_default()

wrapped_text = textwrap.fill(text, width=40)
lines = wrapped_text.split('\n')

img = Image.new("RGB", (width, height), color=background_color)
draw = ImageDraw.Draw(img)

text_height = 0
for line in lines:
    bbox = draw.textbbox((0, 0), line, font=font)
    line_height = bbox[3] - bbox[1]
    text_height += line_height + line_spacing

y_start = (height - text_height) // 2
y = y_start

for line in lines:
    bbox = draw.textbbox((0, 0), line, font=font)
    line_width = bbox[2] - bbox[0]
    line_height = bbox[3] - bbox[1]
    x = (width - line_width) // 2
    draw.text((x, y), line, fill=text_color, font=font)
    y += line_height + line_spacing

img.save("output.png")
print("✅ Image saved as output.png")

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)
print("✅ Text saved as output.txt")

doc = Document()
style = doc.styles['Normal']
font_obj = style.font
font_obj.name = 'Arial'
font_obj.size = Pt(font_size * 0.75)
doc.add_paragraph(text)
doc.save("output.docx")
print("✅ Word document saved as output.docx")

class PDF(FPDF):
    def header(self):
        pass
    def footer(self):
        pass

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Courier", size=12)  # Courier avoids Unicode issues

safe_text = text.replace('’', "'") \
                .replace('‘', "'") \
                .replace('“', '"') \
                .replace('”', '"') \
                .replace('—', '-') \
                .replace('–', '-') \
                .replace('…', '...')

ascii_text = ''.join([ch if ord(ch) < 128 else '?' for ch in safe_text])

pdf_wrapped = textwrap.fill(ascii_text, width=80)
pdf.multi_cell(0, 10, pdf_wrapped)

pdf.output("output.pdf")
print("✅ PDF saved as output.pdf")
