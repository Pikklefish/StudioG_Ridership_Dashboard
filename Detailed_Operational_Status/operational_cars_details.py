import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def operational_cars_details(df_3):
    try:
        nan_mask = df_3['서비스 종료일'].isna()
        filtered_df = df_3[nan_mask]
        filtered_df['운영대수(대)_실시간 호출형'] = filtered_df['운영대수(대)_실시간 호출형'] + filtered_df['운영대수(대)_실시간+고정노선']
        filtered_df['운영대수(대)_고정노선'] = filtered_df['운영대수(대)_고정노선']+ filtered_df['운영대수(대)_예약형'] + filtered_df['운영대수(대)_예약형+고정노선']
        grouped_df = filtered_df.groupby('시군구')[['운영대수(대)_실시간 호출형', '운영대수(대)_고정노선']].sum()

        result = grouped_df.loc[grouped_df.index]

        return result
        
    except Exception as e:
        return st.error(f"Error calculating cars details in operational_cars_details.py: {e}")