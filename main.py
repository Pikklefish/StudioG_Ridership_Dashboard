import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from Helper_Functions.process_uploaded_files import process_uploaded_files
from Helper_Functions.display_dataframes import display_dataframes

def main():
    # Page Config
    st.set_page_config(page_title="바로 Dashboard",
                       page_icon="varo_logo.png",
                       layout="wide"
                       )

    # File Upload and df
    uploaded_files = st.file_uploader("Upload", type="xlsx", accept_multiple_files=True)

    if uploaded_files:
        df_1, df_2, df_3 = process_uploaded_files(uploaded_files)
        display_dataframes(df_1, df_2, df_3)

        
    
    

if __name__ == "__main__":
    main()