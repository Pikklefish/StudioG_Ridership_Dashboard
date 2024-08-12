import streamlit as st


def total_calls_count(df_2):
    try:
        total_calls = 0
        total_calls = df_2['호출 건수(건)'].sum()
        return f"{total_calls:,}"
        
    except Exception as e:
        return st.error(f"Error calculating total calls in total_calls_count.py: {e}")