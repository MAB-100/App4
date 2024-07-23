import pandas as pd
import glob

filepaths = glob.glob('invoices/*.xlsx')
print(filepaths)

for filpath in filepaths:
    df = pd.read_excel(filpath, sheet_name='Sheet 1')
    print(df)
