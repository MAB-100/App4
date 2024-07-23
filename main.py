import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('invoices/*.xlsx')

for filpath in filepaths:
    df = pd.read_excel(filpath, sheet_name='Sheet 1')
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    filename = Path(filpath).stem
    invoice_nr = filename.split('-')[1]
    pdf.set_font('Times', 'B', 16)
    pdf.cell(w = 50, h = 8, txt = f'Invoice nr.{invoice_nr}')
    pdf.output(f"PDFs/{filename}.pdf") 