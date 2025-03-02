import pdfplumber
import csv

pdf_path = "./pdf/runners.pdf"
csv_path = "./csv/runners.csv"

with pdfplumber.open(pdf_path) as pdf:
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                writer.writerows(table)

print("Conversion complete!")
