import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from Helper_Functions.process_uploaded_files import process_uploaded_files
from Helper_Functions.display_dataframes import display_dataframes
from Operational_Status.service_area_count import service_area_count
from Operational_Status.community_count import community_count
from Operational_Status.operational_vehicles_count import operational_vehicles_count

def main():
    # Page Config
    st.set_page_config(page_title="바로 Dashboard",
                       page_icon="varo_logo.png",
                       layout="wide"
                       )

    # File Upload and df
    uploaded_files = st.file_uploader("Upload", type="xlsx", accept_multiple_files=True)

    if uploaded_files:
        df_daily, df_monthly, df_operation = process_uploaded_files(uploaded_files)
        display_dataframes(df_daily, df_monthly, df_operation)
          
        if df_operation is not None:
            service_area= int(service_area_count(df_operation)) 
            st.write("운행지역: ", service_area)
            community= int(community_count(df_operation)) 
            st.write("The community value is: ", community)
            verhicle_count = operational_vehicles_count(df_operation)
            st.write("The number of culumulative vehicles is:",  verhicle_count)
        

        
    
    

if __name__ == "__main__":
    main()