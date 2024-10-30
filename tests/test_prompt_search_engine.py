import pytest
import numpy as np
from search_engine.prompt_search_engine import cosine_similarity, PromptSearchEngine, Vectorizer

def test_cosine_similarity():
    query_vector = np.array([1, 2, 3])
    corpus_vectors = np.array([[1, 0, 0], [0, 1, 0], [1, 1, 0], [1, 2, 3], [4, 5, 6]])
    similarities = cosine_similarity(query_vector, corpus_vectors)
    
    assert np.argmax(similarities) == 3, "Most similar prompt should be at index 3"
    
def test_prompt_search_engine():
    prompts = [
        "What is artificial intelligence?",
        "How does machine learning work?",
        "Tell me about neural networks."
    ]
    
    search_engine = PromptSearchEngine(prompts, model="paraphrase-MiniLM-L6-v2")
    
    results = search_engine.most_similar("What is AI?", n=2)
    allowed_types = (float, np.float32, np.float64)
    
    assert len(results) == 2, "There should be 2 results"
    assert all(isinstance(score, allowed_types) for score, _ in results), "All scores should be floats"
    
def test_vectorizer():
    model = "paraphrase-MiniLM-L6-v2"
    vectorizer = Vectorizer(model)
    prompt = "What is artificial intelligence?"
    
    vector = vectorizer.transform(prompt)
    
    assert len(vector) > 0, "Vector should not be empty"
