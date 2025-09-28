"""
Default Parameters and functions related to changing parameters 
"""


from typing import Dict, List
from copy import deepcopy

# Default parameters
# Visit Neurokit website for parameters: https://neuropsychology.github.io/NeuroKit/_modules/neurokit2/signal/signal_filter.html#signal_filter
# 

base_params = {
    'general': {
        'sampling_frequency': 500,
        'analysis_window_seconds': 30, # calculate HRV metrics in non-overlapping windows.
        'compute_hrv_frequency_metrics': False # might not work if analysis window is short
    },
    'cleaning': {
        'method': 'neurokit',
        'powerline': 50  # or 60
    },
    'peak_detection': {
        'method': 'neurokit',
        'correct_artifacts': True
    },
    'hrv_frequency_settings': {
        'ulf': [0, 0.0033], # The spectral power of ultra low frequencies
        'vlf': [0.0033, 0.04], # The spectral power of very low frequencies
        'lf': [0.04, 0.15], # The spectral power of low frequencies
        'hf': [0.15, 0.4],
        'vhf': [0.4, 0.5], # The spectral power of very high frequencies
        'psd_method': 'welch',
        'normalize': True
    },
    'segmentation': {
        'Baseline': { # name of the segment (does not have to correspond to the name in the event.txt)
            'event_name':'Baseline', # put here the event name from the *event.txt file (e.g., baseline resting start)
            'default_duration_seconds': 300, # put here the duration (in seconds)
            },
        'Story 1': {
            'event_name':'Story 1',
            },
        'Story 2': {
            'event_name':'Story 2',
            },
        'Story 3': {
            'event_name':'Story 3',
            },
        'Story 4': {
            'event_name':'Story 4',
            },
        'Story 5': {
            'event_name':'Story 5',
            },
    }
}


########################################################################################


# Only configure here the parameters to be updated for a given subject if they
# differ from the default parameters specfied above.
def configure_ecg_params(subject_id: int, pipeline_params: Dict) -> List[Dict]:
    """
    Configures and customizes pipeline parameters for ECG processing based on the subject ID.

    This function allows customization of ECG processing parameters for both the child and mother 
    in a subject dyad, based on the unique subject ID. If no customizations are needed, the function 
    returns the default parameters. Subject-specific customizations can be applied by modifying the 
    `pipeline_params` dictionary for each subject.

    Example:
        If the subject has a specific powerline frequency (e.g., 40 instead of the default 50), 
        you can update the 'cleaning' section for the child:

        child_params, mother_params = configure_ecg_params(subject_id=8, pipeline_params=base_params)
        # This will return child_params with updated cleaning parameters:
        # child_params['cleaning']['powerline'] = 40
        
        If another subject requires a different heart rate variability (HRV) calculation, you can modify 
        the 'general' settings for the mother:

        child_params, mother_params = configure_ecg_params(subject_id=4, pipeline_params=base_params)
        # This will return mother_params with custom HRV settings, for example:
        # mother_params['general']['compute_hrv_frequency_metrics'] = True

    Args:
        subject_id (int): The ID of the subject being processed. This ID is used to customize the 
                           pipeline parameters for each subject (child and mother).
        pipeline_params (Dict): The base dictionary containing the default pipeline parameters 
                                 (typically the `base_params` dictionary).

    Returns:
        List[Dict]: A list of two dictionaries, `child_params` and `mother_params`, where both contain 
                    the customized pipeline parameters based on the subject ID.
    """
    child_params = deepcopy(pipeline_params)
    mother_params = deepcopy(pipeline_params)
    
    # Customize parameters based on subject_id
    # if subject_id == 8:
    #     child_params['cleaning'].update({"powerline": 40})

    # elif subject_id == "4":
    #     mother_params['general'].update({"key2": "value2"})
    
    # Add more conditions for other subject IDs as needed

    return child_params, mother_params



def configure_segmentation_params(subject_id: int, pipeline_params: Dict) -> Dict:
    """
    Configures segmentation parameters based on the subject ID. Note that segmentation settings 
    cannot be customized separately for the child and mother; the same settings are applied to both.

    This function allows customization of segmentation parameters such as event onset and duration 
    for different phases of the study. Customizations can be made based on the subject ID. If no changes 
    are needed, the default segmentation parameters are returned.

    Example:
        To update the duration of the baseline segment for a specific subject (e.g., subject 8), 
        you can update the segmentation parameters:

        parameters = configure_segmentation_params(subject_id=8, pipeline_params=base_params)
        # This will return the segmentation parameters with an updated duration for 'baseline':
        # parameters['segmentation']['baseline']['duration'] = 250
        
        If no changes are required, the default segmentation parameters are used:
        
        parameters = configure_segmentation_params(subject_id=10, pipeline_params=base_params)
        # This will return the default segmentation parameters as specified in base_params.

    Args:
        subject_id (int): The ID of the subject being processed. This ID is used to customize the 
                           segmentation parameters.
        pipeline_params (Dict): The base dictionary containing the default pipeline parameters 
                                 (typically the `base_params` dictionary).

    Returns:
        Dict: The customized segmentation parameters based on the subject ID. 
              If no customizations are made, the default segmentation settings are returned.
    """
    parameters = deepcopy(pipeline_params)
    
    # Customize parameters based on subject_id
    # if subject_id == 8:
    #     parameters['segmentation']['baseline'].update({"duration": 250})
    
    # Add more conditions for other subject IDs as needed

    return parameters
