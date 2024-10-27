import numpy as np
from sentence_transformers import SentenceTransformer
from typing import Sequence, List, Tuple
import pickle

class Vectorizer:
    def __init__(self, model: str) -> None:
        """
        Initialize the vectorizer with a pre-trained embedding model.

        Args:
            model (str): The pre-trained embedding model to use for transforming prompts.
        """
        self.model = SentenceTransformer(model)

    def transform(self, prompt: str):
        """
        Transform a textual prompt into a numerical vector representation.

        Args:
            prompt (str): The textual prompt to be transformed.

        Returns:
            numpy.ndarray: The numerical vector representation of the prompt.
            """
        return self.model.encode(prompt)


def cosine_similarity(
    query_vector: np.ndarray,
    corpus_vectors: np.ndarray
) -> np.ndarray:
    """
    Calculate cosine similarity between the query vector and corpus vectors.

    Args:
        query_vector (np.ndarray): Vectorized prompt query of shape (1, D).
        corpus_vectors (np.ndarray): Vectorized prompt corpus of shape (N, D).

    Returns:
        np.ndarray: A vector of shape (N,) with cosine similarity scores in the range [-1, 1].
    """
        # Validate that inputs are numpy arrays
    if not isinstance(query_vector, np.ndarray):
        raise ValueError("query_vector must be a numpy array.")

    if not isinstance(corpus_vectors, np.ndarray):
        raise ValueError("corpus_vectors must be a numpy array.")

    # Check for NaN or Inf values
    if np.isnan(query_vector).any() or np.isinf(query_vector).any():
        raise ValueError("query_vector contains NaN or Inf values.")

    if np.isnan(corpus_vectors).any() or np.isinf(corpus_vectors).any():
        raise ValueError("corpus_vectors contains NaN or Inf values.")

    # Normalize the query vector and corpus vectors to unit vectors
    query_norm = np.linalg.norm(query_vector)
    corpus_norms = np.linalg.norm(corpus_vectors, axis=1)

    # Calculate the dot product between the query vector and each vector in the corpus
    dot_products = np.dot(corpus_vectors, query_vector)

    # Compute cosine similarity, epsilon is added for stability
    epsilon=1e-4
    cosine_similarities = dot_products / (query_norm * corpus_norms+epsilon)

    return cosine_similarities


class PromptSearchEngine:
    def __init__(self, prompts: Sequence[str], model: str) -> None:
        """
        Initialize the search engine by vectorizing the prompt corpus.
        Vectorized prompt corpus should be used to find the top n most
        similar prompts w.r.t. the user’s input prompt.

        Args:
            prompts (Sequence[str]): The sequence of raw prompts from the dataset.
            model (str): The pre-trained model to be used for vectorizing.
        """
        if not prompts:
            raise ValueError("The prompt corpus is empty.")
        self.prompts = prompts
        self.vectorizer = Vectorizer(model)
        # Vectorize the entire corpus during initialization
        self.corpus_vectors = np.array([self.vectorizer.transform(prompt) for prompt in prompts])

    def most_similar(self, query: str, n: int = 5) -> List[Tuple[float, str]]:
        """
        Return the top n most similar prompts from the corpus.
        Input query prompt should be vectorized using the Vectorizer.
        Then, use the cosine_similarity function to find the most similar
        prompts from the corpus.

        Args:
            query (str): The raw query prompt input from the user.
            n (int): The number of similar prompts to return.

        Returns:
            List[Tuple[float, str]]: A list of top n most similar prompts from the corpus along with similarity scores.
        """
        if not query:
            raise ValueError("The query prompt is empty.")
        if n<=0:
            raise ValueError("n must be positive number.")
        # Vectorize the query prompt
        query_vector = self.vectorizer.transform(query)

        # Calculate cosine similarities between the query and corpus
        similarity_scores = cosine_similarity(query_vector, self.corpus_vectors)

        # Get the indices of the top n most similar prompts
        top_n_indices = np.argsort(similarity_scores)[::-1][:n]

        # Return the top n prompts and their similarity scores
        return [(similarity_scores[i], self.prompts[i]) for i in top_n_indices]