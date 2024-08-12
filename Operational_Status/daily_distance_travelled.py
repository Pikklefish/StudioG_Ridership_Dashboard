import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from datetime import timedelta

def daily_distance_travelled(df_1, targetdate):
    try:
        targetdate = targetdate - timedelta(days=1)
        daily_distance = 0
    
        df_1['날짜'] = pd.to_datetime(df_1['날짜'], format="%Y-%m-%d")

        masked_df_1 = df_1[df_1['날짜'] == targetdate]
        st.dataframe(masked_df_1)

        daily_call = masked_df_1['운행 거리(km)'].sum()
        return f"{daily_call:,}"
    
    except Exception as e:
        return st.error(f"Error calculating daily rider count in daily_distance_travelled.py: {e}")