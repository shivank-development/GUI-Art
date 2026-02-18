from fpdf import FPDF
name = "John Doe"

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", "B", 24)
pdf.text(40, 80, "Certificate of Completion")

pdf.set_font("Arial", "", 18)
pdf.text(40, 100, f"Presented to {name}")
# You can customize the position and styling as needed
pdf.output("certificate.pdf")
print("PDF certificate generated successfully.")