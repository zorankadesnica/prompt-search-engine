# Prompt Search Engine

![Example query prompt](images/corgi.png)

The **Prompt Search Engine** is an application that allows users to input a query prompt and retrieve the top `n` most similar prompts from a dataset. It uses **Sentence-BERT (SBERT)** for vectorizing prompts and **cosine similarity** to compute prompt similarity.The use case is for Stable Diffusion- search engine  assists in generating better prompts by leveraging a database of existing prompts.These prompts significantly impact the quality and relevance of the generated images.

## Features
- Vectorizes input prompts and dataset prompts using SBERT.
- Computes cosine similarity to find the top `n` most similar prompts.
- Provides a FastAPI-based API for backend.
- Includes a user-friendly frontend built with Streamlit.
  
In this example, we serve an sentence-transformers model using FastAPI for the backend service and streamlit for the frontend service.
Docker compose orchestrates the two services and allows communication between them.
## Run it loccaly
To run the example in a machine running Docker and docker compose, do following steps:

1. Clone the repository:
```bash
   git clone https://github.com/zorankadesnica/prompt-search-engine.git
```

2.  Navigate to the project directory:
```bash
cd prompt-search-engine-sd
```
3. Create a virtual environment:
python -m venv venv

4. Activate the virtual environment:

- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```
5. 
```bash
docker compose build
docker compose up
```
6. Open  [localhost:8501](localhost:8501) on your browser and you can play with your personal prompts for stable diffusion and see how similar they are with corpus prompts.
Playground.py is toy example of how prompt search engine works.
