#fmt:off
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent)) # the dir containing utils
import ecg_utils.parameters as params
import ecg_utils.common as common
import ecg_utils.nk_pipeline as nk_pipeline
import ecg_utils.data_utils as data_utils
import numpy as np
import pandas as pd
from datetime import datetime
import traceback
from typing import Dict, Union, Optional, List, Tuple
#fmt:on

    
def compute_windowed_hrv_across_segments(
    segments_df_list: List[pd.DataFrame], 
    parameters: Dict, 
    figure_output_dir: Union[str, Path], 
    data_output_dir: Union[str, Path], 
    subject_id: Union[str, int],
    create_qa_plots:bool=True
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Compute windowed Heart Rate Variability (HRV) metrics across multiple ECG data segments.

    This function iterates through a list of segmented ECG DataFrames, calculates windowed HRV metrics 
    for each segment, and optionally generates quality assurance (QA) plots for each segment. The HRV 
    metrics and preprocessed ECG data are saved to specified output directories and returned as concatenated 
    DataFrames.

    Args:
        segments_df_list (List[pd.DataFrame]): A list of DataFrames, where each DataFrame represents
            a segment of ECG data. Each segment must contain an `event_name` column identifying the segment.
        parameters (Dict): A dictionary containing configuration parameters for HRV calculations, such as 
            window length and sampling frequency.
        figure_output_dir (Union[str, Path]): Directory to save QA plots, if `create_qa_plots` is True.
        data_output_dir (Union[str, Path]): Directory to save the output HRV metrics and preprocessed ECG data.
        subject_id (Union[str, int]): Unique identifier for the subject to which the segments belong.
        create_qa_plots (bool, optional): If True, generates and saves QA plots for each segment. Defaults to True.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: 
            - A DataFrame containing concatenated HRV metrics for all segments, with `segment_name` 
              and `subject_id` columns added.
            - A DataFrame containing concatenated preprocessed ECG data for all segments, with `segment_name` 
              and `subject_id` columns added.

    Raises:
        ValueError: If the input `segments_df_list` does not contain valid segments or required columns.

    Example:
        >>> import pandas as pd
        >>> from pathlib import Path
        >>> segments = [segment1, segment2]  # List of segmented ECG DataFrames
        >>> parameters = {"general": {"sampling_frequency": 500, "window_length": 60}}
        >>> figure_dir = Path("./output/figures")
        >>> data_dir = Path("./output/data")
        >>> subject_id = "12345"
        >>> hrv_metrics, preprocessed_data = compute_windowed_hrv_across_segments(
        ...     segments, parameters, figure_dir, data_dir, subject_id, create_qa_plots=True
        ... )
        >>> print(hrv_metrics.head())
        >>> print(preprocessed_data.head())

    Notes:
        - The function assumes that the `nk_pipeline.calculate_windowed_HRV_metrics` is available 
          for calculating HRV metrics.
        - HRV metrics are saved in an Excel file named `hrv_metrics.xlsx`.
        - Preprocessed ECG data is saved in a CSV file named `preprocessed_ecg.csv`.

    """
    figure_output_dir = Path(figure_output_dir)
    data_output_dir = Path(data_output_dir)
    
    all_hrv_metrics = []
    all_preprocessed_data = []

    for segment_df in segments_df_list:
        segment_name = segment_df["event_name"].iloc[0]
        hrv_segment_metrics_df = nk_pipeline.calculate_windowed_HRV_metrics(
            segment_df, 
            parameters, 
            export_segment_plot=create_qa_plots,
            figure_output_dir=figure_output_dir, 
            segment_name=segment_name
        )
        
        # Add HRV metrics and preprocessed data to lists
        hrv_segment_metrics_df = hrv_segment_metrics_df.assign(segment_name = segment_name)
        all_hrv_metrics.append(hrv_segment_metrics_df)
        segment_df = segment_df.assign(segment_name = segment_name)
        all_preprocessed_data.append(segment_df)

    # Concatenate all HRV metrics and preprocessed data
    concatenated_hrv_metrics = pd.concat(all_hrv_metrics, ignore_index=True)
    concatenated_hrv_metrics = concatenated_hrv_metrics.assign(subject_id = subject_id)
    concatenated_preprocessed_data = pd.concat(all_preprocessed_data, ignore_index=True)
    concatenated_preprocessed_data = concatenated_preprocessed_data.assign(subject_id = subject_id)
    
    # save the data
    concatenated_hrv_metrics.to_excel(data_output_dir / "hrv_metrics.xlsx")
    concatenated_preprocessed_data.to_csv(data_output_dir / "preprocessed_ecg.csv")

    return concatenated_hrv_metrics, concatenated_preprocessed_data
        


if __name__ == "__main__":
    pass