import pandas as pd
import plotly.express as px

def status_handler(file):
    df = pd.read_excel(
        io=file,
        engine='openpyxl',
        sheet_name='DRT 서비스 현황',
        skiprows=0,
        usecols='A:H',
    )
    return df