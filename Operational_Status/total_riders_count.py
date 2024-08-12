import streamlit as st

def total_riders_count(df_2):
    try:
        total_riders = 0
        total_riders = df_2['이용인원(인)'].sum()
        return f"{total_riders:,}"
        
    except Exception as e:
        return st.error(f"Error calculating total riders in total_riders_count.py: {e}")
      