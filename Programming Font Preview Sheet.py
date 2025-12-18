from fpdf import FPDF

fonts = ["Arial", "Courier", "Times"]

pdf = FPDF()
pdf.add_page()

for f in fonts:
    pdf.set_font(f, size=16)
    pdf.cell(0, 10, f"{f} font sample", ln=True, border=1)

pdf.output("fonts_preview.pdf")
