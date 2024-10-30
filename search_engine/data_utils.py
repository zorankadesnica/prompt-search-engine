from urllib.request import urlretrieve
import pandas as pd

def load_prompts_data(parquet_file_path:str,  n_of_prompts: int = 1000) -> list:
    """
    Load prompts  stored in a Parquet file.
    
    Args:
        parquet_file_path: The path to the Parquet file containing the dataset.
        num_prompts: The number of prompts to return.
        
    Returns:
        A list of prompts.
    """
    # Ensure the parquet_file_path is a string
    if not isinstance(parquet_file_path, str):
        raise ValueError(f"Expected 'parquet_file_path' to be a string, got {type(parquet_file_path).__name__}")

    # Download the parquet table
    urlretrieve(parquet_file_path, 'metadata.parquet')
      
    # Read only the 'prompt' column from the downloaded parquet file and get the first n rows
    metadata_df = pd.read_parquet('metadata.parquet', columns=['prompt'])
    
    # Ensure n_of_prompts does not exceed the number of available prompts
    available_prompts = len(metadata_df)
    if n_of_prompts > available_prompts:
        n_of_prompts = available_prompts
        
    prompts_list = metadata_df['prompt'].head(n_of_prompts).tolist()
    
    return prompts_list

    
   