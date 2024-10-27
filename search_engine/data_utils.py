from urllib.request import urlretrieve
import pandas as pd

#DiffusionDB is the first large-scale text-to-image prompt dataset. 
def load_prompts_data( n_of_prompts: int = 1000) -> list:
    # Download the parquet table
    table_url = f'https://huggingface.co/datasets/poloclub/diffusiondb/resolve/main/metadata.parquet'
    urlretrieve(table_url, 'metadata.parquet')
    
    # Read only the 'prompt' column from the downloaded parquet file and get the first n rows
    metadata_df = pd.read_parquet('metadata.parquet', columns=['prompt'])
    prompts_list = metadata_df['prompt'].head(n_of_prompts).tolist()
    
    return prompts_list

    
   