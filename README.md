# Prompt Search Engine

## Overview
The **Prompt Search Engine** is an application that allows users to input a query prompt and retrieve the top `n` most similar prompts from a dataset. It uses **Sentence-BERT (SBERT)** for vectorizing prompts and **cosine similarity** to compute prompt similarity. The app consists of a FastAPI backend and a Streamlit-based UI.

## Features
- Vectorizes input prompts and dataset prompts using SBERT.
- Computes cosine similarity to find the top `n` most similar prompts.
- Provides a FastAPI-based API for backend.
- Includes a user-friendly frontend built with Streamlit.
- 
In this example, we serve an sentence-transformers model using FastAPI for the backend service and streamlit for the frontend service.
docker compose orchestrates the two services and allows communication between them.
To run the example in a machine running Docker and docker compose, run:

```bash

docker compose build
docker compose up
```

Playground.py is toy example of how prompt search engine works.
