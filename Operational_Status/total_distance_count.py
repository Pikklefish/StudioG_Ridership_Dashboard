import streamlit as st

def total_distance_count(df_2):
    try:
        total_dist = 0
        total_dist = round(df_2['운행 거리(km)'].sum())
        return f"{total_dist:,}"
    
    except Exception as e:
        return st.error(f"Error calculating total distance in total_distance_count.py: {e}")       


    