from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Tuple
from prompt_search_engine import PromptSearchEngine
from data_utils import load_prompts_data

# Initialize FastAPI app
app = FastAPI()

# Number of prompts in corpus 
n_of_prompts_corpus=1000

#load prompts in corpus:
url = f'https://huggingface.co/datasets/poloclub/diffusiondb/resolve/main/metadata.parquet'
prompts=load_prompts_data(url,n_of_prompts_corpus)

# Initialize the PromptSearchEngine with a default model and prompt dataset 
search_engine = PromptSearchEngine(prompts=prompts, model='paraphrase-MiniLM-L6-v2')

# Pydantic model to define the structure of input
class QueryInput(BaseModel):
    query: str
    n: int = 5  # Default to top 5 similar prompts

# Pydantic model to define the structure of output
class SimilarPrompt(BaseModel):
    similarity_score: float
    prompt: str

@app.post("/search/", response_model=List[SimilarPrompt])
async def search_similar_prompts(query_input: QueryInput):
    """
    API endpoint to search for the most similar prompts from the corpus.
    
    Args:
        query_input (QueryInput): The query prompt and number of similar prompts to return.
        
    Returns:
        List of top n most similar prompts along with similarity scores.
    """
    try:
        # Extract query and n from the input
        query = query_input.query
        n = query_input.n
        
        # Get the top n most similar prompts
        results = search_engine.most_similar(query=query, n=n)
        
        # Format the response
        response = [{"similarity_score": score, "prompt": prompt} for score, prompt in results]
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
