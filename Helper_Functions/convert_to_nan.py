import pandas as pd
import numpy as np

def convert_to_nan(df):
    """Replace '-' with NaN in the DataFrame."""
    df.replace("-", np.nan, inplace=True)
    return df