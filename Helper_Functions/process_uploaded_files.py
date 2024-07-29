import streamlit as st
import pandas as pd
import numpy as np

from Data_Handlers.daily_handler import daily_handler
from Data_Handlers.monthly_handler import monthly_handler
from Data_Handlers.status_handler import status_handler
from Data_Handlers.file_type_handler import file_type_handler

from Helper_Functions.convert_to_nan import convert_to_nan

def process_uploaded_files(uploaded_files):
    """Process the uploaded files and return the dataframes."""
    df_1, df_2, df_3 = None, None, None
    df2s = []

    for uploaded_file in uploaded_files:
        filename = uploaded_file.name
        file_type = file_type_handler(filename)
        
        if file_type == "type_1":
            df_1 = convert_to_nan(daily_handler(uploaded_file))

        elif file_type == "type_2":
            df_2 = convert_to_nan(monthly_handler(uploaded_file))
            df2s.append(df_2)
        elif file_type == "type_3":
            df_3 = convert_to_nan(status_handler(uploaded_file))
        else:
            e = " in process_uploaded_files"
            st.error(file_type + e)
            continue
    
    if df2s:
        df_2 = pd.concat(df2s, ignore_index=True)

    return df_1, df_2, df_3