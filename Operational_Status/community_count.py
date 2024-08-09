import pandas as pd

def community_count(df_3):
    int_total_count = 0

    nan_mask = df_3['서비스 종료일'].isna()
    masked_df_3 = df_3[nan_mask]           #filters df_3 to rows that only have nan_mask as `True`

    for value in masked_df_3['읍면동']:
        if pd.notna(value):
            int_total_count+=1
        if isinstance(value, str) and '/' in value:
           int_total_count += value.count('/') + 1

    return int_total_count



