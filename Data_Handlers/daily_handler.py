import pandas as pd
import plotly.express as px


def daily_handler(file):
    df = pd.read_excel(
        io=file,
        engine='openpyxl',
        sheet_name='전체',
        skiprows=0,
    )
    return df