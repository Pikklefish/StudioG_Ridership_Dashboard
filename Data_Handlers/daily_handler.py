import pandas as pd

def daily_handler(file):
    df = pd.read_excel(
        io=file,
        engine='openpyxl',
        sheet_name='전체',
    )
    return df