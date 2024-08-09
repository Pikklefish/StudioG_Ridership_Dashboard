import streamlit as st

def operational_vehicles_count(df_3):
    try: 
        total_cars = 0

        nan_mask = df_3['서비스 종료일'].isna()
        masked_df_3 = df_3[nan_mask]           #filters df_3 to rows that only have nan_mask as `True`
        total_cars = masked_df_3['운영대수(대)_합계'].sum()

        return total_cars

    except Exception as e:
         return st.error(f"Error calculating operational vehicle count in operational_vehicles_count.py: {e}")
        