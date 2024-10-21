# Prompt Search Engine

## Overview
The **Prompt Search Engine** is an application that allows users to input a query prompt and retrieve the top `n` most similar prompts from a dataset. It uses **Sentence-BERT (SBERT)** for vectorizing prompts and **cosine similarity** to compute prompt similarity. The app consists of a FastAPI backend and a Streamlit-based UI.

## Features
- Vectorizes input prompts and dataset prompts using SBERT.
- Computes cosine similarity to find the top `n` most similar prompts.
- Provides a FastAPI-based API for backend.
- Includes a user-friendly frontend built with Streamlit.

  ##Code structure
  prompt_search_engine_project/
│
├── app/
│   ├── __init__.py
│   ├── vectorizer.py
│   ├── cosine_similarity.py
│   ├── search_engine.py
│
├── tests/
│   ├── __init__.py
│   ├── test_vectorizer.py
│   ├── test_cosine_similarity.py
│   ├── test_search_engine.py
│
├── run.py
├── requirements.txt
├── Dockerfile
├── README.md
├── streamlit_app.py

