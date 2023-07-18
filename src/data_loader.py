import pandas as pd
import pickle


def load_data(file_path):
    """
    Load data from a CSV file and return a pandas DataFrame.
    
    Parameters:
    - file_path (str): The path to the CSV file.
    
    Returns:
    - df (pandas.DataFrame): The loaded data as a DataFrame.
    """
    df = pd.read_csv(file_path)
    return df

def save_data_as_pickle(data, file_path):
    """
    Save data as a pickle file.
    
    Parameters:
    - data: The data to be saved.
    - file_path (str): The path to save the pickle file.
    """
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

def load_data_from_pickle(file_path):
    """
    Load data from a pickle file.
    
    Parameters:
    - file_path (str): The path to the pickle file.
    
    Returns:
    - data: The loaded data.
    """
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data
