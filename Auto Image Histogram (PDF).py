import cv2
import matplotlib.pyplot as plt
from fpdf import FPDF

# Read image in grayscale
img = cv2.imread("bird.jpg", 0)

# Safety check
if img is None:
    print("Image not found!")
    exit()

# Create and save histogram
plt.hist(img.ravel(), 50)
plt.title("Image Intensity Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.savefig("hist.png")
plt.close()

# Create PDF report
pdf = FPDF()
pdf.add_page()
pdf.image("hist.png", x=20, y=20, w=160)
pdf.output("hist_report.pdf")
print("PDF report with histogram generated successfully.")