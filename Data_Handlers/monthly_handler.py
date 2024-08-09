import pandas as pd

def monthly_handler(file):
    df = pd.read_excel(
        io=file,
        engine='openpyxl',
        sheet_name='전체',
        skiprows=0,
        usecols='A:AD',
    )
    return df