import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from datetime import timedelta

def daily_calls_count(df_1, targetdate):
    try:
        targetdate = targetdate - timedelta(days=1)
        daily_calls = 0
    
        df_1['날짜'] = pd.to_datetime(df_1['날짜'], format="%Y-%m-%d")

        masked_df_1 = df_1[df_1['날짜'] == targetdate]
        st.dataframe(masked_df_1)

        daily_call = masked_df_1['[합계] 호출·예약 건수(건)'].sum()
        return f"{daily_call:,}"
    
    except Exception as e:
        return st.error(f"Error calculating daily rider count in daily_call_count.py: {e}")