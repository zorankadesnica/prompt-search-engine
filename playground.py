from search_engine import prompt_search_engine
import numpy as np


# Sample prompts dataset
prompts = [
    "What is artificial intelligence?",
    "How does machine learning work?",
    "Tell me about neural networks.",
    "Explain the concept of deep learning.",
    "What is AI used for?"
]

# Create an instance of the PromptSearchEngine with a pre-trained SBERT model
search_engine = prompt_search_engine.PromptSearchEngine(prompts, 'paraphrase-MiniLM-L6-v2')

# Query prompt
query_prompt = "What is AI?"

# Get the top 3 most similar prompts from the corpus
top_similar_prompts = search_engine.most_similar(query_prompt, n=4)

# Print results
for score, prompt in top_similar_prompts:
    print(f"Similarity Score: {score:.4f}, Prompt: {prompt}")
