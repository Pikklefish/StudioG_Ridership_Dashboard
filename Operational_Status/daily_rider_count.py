import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from datetime import timedelta

def daily_rider_count(df_1, targetdate):
    try:
        targetdate = targetdate - timedelta(days=1)
        daily_rider = 0

        df_1['날짜'] = pd.to_datetime(df_1['날짜'], format="%Y-%m-%d")

        masked_df_1 = df_1[df_1['날짜'] == targetdate]
        st.dataframe(masked_df_1)

        daily_rider = masked_df_1['[합계] 이용인원(인)'].sum()
        return daily_rider
    
    except Exception as e:
        return st.error(f"Error calculating daily rider count in daily_rider_count.py: {e}")