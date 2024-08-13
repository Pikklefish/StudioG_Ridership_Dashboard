import streamlit as st
import pandas as pd

def monthly_usage_status(df_2):
    try:
        df_2['년월'] = pd.to_datetime(df_2['년월'], format='%Y-%m')
        last_month = df_2['년월'].max()
        cutoff_month = last_month-pd.DateOffset(months=4)
        filtered_df = df_2[(df_2['년월'] >= cutoff_month) & (df_2['년월'] <= last_month)]
        grouped_df = filtered_df.groupby(df_2['년월'].dt.to_period('M'))['이용완료 건수(건)'].sum().reset_index()
        grouped_df['년월'] = grouped_df['년월'].dt.to_timestamp()

        return grouped_df
    
    except Exception as e:
        return st.error(f"Error calculating monthly riders in monthly_usage_status.py: {e}")
