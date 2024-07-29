import streamlit as st
import pandas as pd
import plotly.express as px
from Data_Handlers.daily_handler import daily_handler
from Data_Handlers.monthly_handler import monthly_handler
from Data_Handlers.file_type_handler import file_type_handler
from Streamlit_Components.side_bar import side_bar

def main():
    # Page Config
    st.set_page_config(page_title="바로 Dashboard",
                       page_icon="varo_logo.png",
                       layout="wide"
                       )

    # File Upload and df
    uploaded_files = st.file_uploader("Upload", type="xlsx", accept_multiple_files=True)

    if uploaded_files:
        dfs=[]
        for uploaded_file in uploaded_files:
            filename = uploaded_file.name
            file_type = file_type_handler(filename)
            if file_type == "type_1":
                df = daily_handler(uploaded_file)
            elif file_type == "type_2":
                df = monthly_handler(uploaded_file)
            else:
                st.error(file_type)
                continue
            st.write(f"Processed data for file: {filename}")
            st.dataframe(df)
            dfs.append(df)
    
    



if __name__ == "__main__":
    main()