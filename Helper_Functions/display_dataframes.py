import streamlit as st

def display_dataframes(df_1, df_2, df_3):
    """Display the dataframes in the Streamlit app."""
    if df_1 is not None:
        st.write("Daily Data")
        st.dataframe(df_1)
    
    if df_2 is not None:
        st.write("Concatenated Monthly Data")
        st.dataframe(df_2)

    if df_3 is not None:
        st.write("Status Data")
        st.dataframe(df_3)

