import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('invoices/*.xlsx')

for filpath in filepaths:
    
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    
    
    filename = Path(filpath).stem
    
    invoice_nr = filename.split('-')[0]
    invoice_dt = filename.split('-')[1]
    
    pdf.set_font('Times', 'B', 16)
    pdf.cell(w = 50, h = 8, txt = f'Invoice nr.{invoice_nr}', ln=1)
    pdf.cell(w = 50, h = 8, txt = f'Date {invoice_dt}', ln=1)

    df = pd.read_excel(filpath, sheet_name='Sheet 1')

    #add a header
    columns = list(df.columns)
    columns = [item.replace('_', ' ').title() for item in columns]

    pdf.set_font(family='Times', size= 12, style='B')
    pdf.cell(w = 30, h = 8, txt = columns[0], border=1)
    pdf.cell(w = 70, h = 8, txt = columns[1], border=1)
    pdf.cell(w = 40, h = 8, txt = columns[2], border=1)
    pdf.cell(w = 30, h = 8, txt = columns[3], border=1)
    pdf.cell(w = 30, h = 8, txt = columns[4], border=1, ln=1)

    #add rows
    for index , row in df.iterrows():
        pdf.set_font(family='Times', size= 12)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w = 30, h = 8, txt = str(row['product_id']), border=1)
        pdf.cell(w = 70, h = 8, txt = str(row['product_name']), border=1)
        pdf.cell(w = 40, h = 8, txt = str(row['amount_purchased']), border=1)
        pdf.cell(w = 30, h = 8, txt = str(row['price_per_unit']), border=1)
        pdf.cell(w = 30, h = 8, txt = str(row['total_price']), border=1, ln=1)

    # total row
    total = df["total_price"].sum()
    pdf.set_font(family='Times', size= 12)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w = 30, h = 8, txt = "", border=1)
    pdf.cell(w = 70, h = 8, txt = "", border=1)
    pdf.cell(w = 40, h = 8, txt = "", border=1)
    pdf.cell(w = 30, h = 8, txt = "", border=1)
    pdf.cell(w = 30, h = 8, txt = str(total), border=1, ln=1)

    # total sum sentence
    pdf.set_font(family='Times', size= 12, style='B')
    pdf.cell(w = 30, h = 8, txt =f"The toal price is {total}", ln=1)

    # company name and logo
    pdf.set_font(family='Times', size= 12, style='B')
    pdf.cell(w = 20, h = 8, txt =f"CureMD")
    pdf.image("logo.png", w=10)


    pdf.output(f"PDFs/{filename}.pdf") 