import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

#Read in Data from XLSX

excel_title = "전국 (2024-06-18).xlsx"
# input("Enter the Excel Sheet name: ")
sheet_name = "나주(평일)"
# input("Enter the name of the specific sheet: ")

data_frame = pd.read_excel(excel_title, header=1, engine = 'openpyxl', sheet_name= sheet_name, index_col=0)
print(data_frame.head())
print(data_frame.columns)

# Ensure the index is datetime
data_frame.index = pd.to_datetime(data_frame.index, errors='coerce')
print(len(data_frame.index))

# If NaT exists, identify
nat_rows = data_frame.index.isna()
for i, is_na in enumerate(nat_rows):
    if is_na:
        print(f"Date conversion incorrect on row: {i}")

