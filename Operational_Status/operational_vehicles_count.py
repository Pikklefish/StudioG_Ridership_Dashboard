import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from datetime import datetime, timedelta

def operational_vehicles_count(df_3):
    total_cars = 0

    nan_mask = df_3['서비스 종료일'].isna()
    masked_df_3 = df_3[nan_mask]           #filters df_3 to rows that only have nan_mask as `True`
    total_cars = masked_df_3['합계)'].sum()

    return total_cars
