import pandas as pd
from pathlib import Path
import numpy as np
from typing import Union, List



def flag_windows_insufficient_n_peaks(metrics_df: pd.DataFrame, min_peaks_required: int = 20) -> pd.DataFrame:
    """
    Flags HRV analysis windows based on the number of detected peaks.

    This function evaluates whether each window in the given DataFrame has a sufficient number 
    of peaks detected. It creates a new column, 'window_has_enough_peaks', and assigns a 
    boolean value indicating whether the window meets the minimum required peaks.

    Args:
        hrv_metrics_df (pd.DataFrame): DataFrame containing HRV metrics, including a 
            column 'n_peaks_detected' which indicates the number of peaks detected in each window.
        min_peaks_required (int, optional): Minimum number of peaks required for a window 
            to be considered valid. Defaults to 20.

    Returns:
        pd.DataFrame: Updated DataFrame with a new column 'window_has_enough_peaks' 
        containing boolean values where:
            - True: The window has sufficient peaks (>= min_peaks_required).
            - False: The window has insufficient peaks (< min_peaks_required).
    """
    condition = metrics_df.n_peaks_detected < min_peaks_required
    metrics_df["window_has_enough_peaks"] = np.where(
        condition,
        False,
        True
    )
    return metrics_df



def flag_outliers_based_on_zscore(
    df: pd.DataFrame, 
    column: str, 
    z_threshold: float
) -> pd.DataFrame:
    """
    Flags outliers in a column based on a z-score approach, considering only rows 
    where 'window_has_enough_peaks' is True.

    Args:
        df (pd.DataFrame): The input DataFrame.
        column (str): The name of the column for outlier detection.
        z_threshold (float): The z-score threshold above which a value is flagged as an outlier.

    Returns:
        pd.DataFrame: The original DataFrame with a new column indicating outliers.
                      The new column name is the input column name plus '_outlier'.
    """
    # Ensure 'window_has_enough_peaks' exists in the DataFrame
    if "window_has_enough_peaks" not in df.columns:
        raise ValueError("The DataFrame must contain a 'window_has_enough_peaks' column.")
    
    # Compute the z-score only for rows where 'window_has_enough_peaks' is True
    valid_rows = df["window_has_enough_peaks"] == True
    values = df.loc[valid_rows, column]
    z_scores = (values - values.mean()) / values.std(ddof=0)
    
    # Create the new column name
    outlier_column_name = f"{column}_outlier"
    
    # Initialize the new column with NaN (explicitly setting dtype to float)
    df[outlier_column_name] = np.nan
    
    # Flag outliers as True/False and cast to float to align with NaN dtype
    df.loc[valid_rows, outlier_column_name] = (np.abs(z_scores) > z_threshold).astype(float)
    
    return df


def flag_usable_aggregation_windows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a column to the DataFrame indicating whether or not an analysis window can be used for aggregation of HRV and RSA values. 
    If an analyis window cannot be used (e.g., due to insufficient peaks or outlier detection), the window is flagged as not usable.
    Note that a new column usable_window is added to the DataFrame. That approach will be used for filtering HRV and RSA values before aggregation. 
    

    A window is considered usable if:
    - 'window_has_enough_peaks' is True
    - 'HRV_SDNN_outlier' is 0.0

    Args:
        df (pd.DataFrame): The input DataFrame containing 'window_has_enough_peaks' 
                           and 'HRV_SDNN_outlier' columns.

    Returns:
        pd.DataFrame: The original DataFrame with a new boolean column 'usable_window'.
    """
    # Ensure necessary columns exist
    required_columns = ["window_has_enough_peaks", "HRV_SDNN_outlier"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"The DataFrame must contain the column '{col}'.")

    # Add the new column
    df["usable_window"] = (df["window_has_enough_peaks"] == True) & (df["HRV_SDNN_outlier"] == 0.0)

    return df
