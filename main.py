import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

#Read in Data from XLSX

excel_title = input("Enter the Excel Sheet name: ")
cols = ["이용완료", "이용인원", "호출건수", "평균대기시간 (제시)", "운행거리", "우회거리율","우회시간율","평균탑승인원", "평균탑승인원	인km/대시"]
data_frame = pd.read_excel(excel_title, names=cols, engine = 'openpyxl', sheet_name=1)
print(data_frame.head())