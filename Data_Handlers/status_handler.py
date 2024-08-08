import pandas as pd
import plotly.express as px
import streamlit as st

def status_handler(file):
    try:
        df = pd.read_excel(
            io=file,
            engine='openpyxl',
            sheet_name='DRT 서비스 현황(세부)',
            header=[0, 1]
        )
        df.columns = ['_'.join(col).strip() if 'Unnamed' not in col[1] else col[0] for col in df.columns.values]

        return df
    
    except Exception as e:

        return st.error(f"Error reading Excel file in status_handler.py: {e}")