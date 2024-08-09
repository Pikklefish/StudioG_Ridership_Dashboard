import streamlit as st


def service_area_count(df_3):
    try:
        int_total_count = 0

        nan_mask = df_3['서비스 종료일'].isna()
        masked_df_3 = df_3[nan_mask]           #filters df_3 to rows that only have nan_mask as `True`
        int_total_count = masked_df_3['시군구'].nunique()

        return int_total_count

    except Exception as e:
        return st.error(f"Error calculating service area in service_area_count.py: {e}")
    
    
    
    


