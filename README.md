# Prompt Search Engine

## Overview
The **Prompt Search Engine** is an application that allows users to input a query prompt and retrieve the top `n` most similar prompts from a dataset. It uses **Sentence-BERT (SBERT)** for vectorizing prompts and **cosine similarity** to compute prompt similarity. The app consists of a FastAPI backend and a Streamlit-based UI.

## Features
- Vectorizes input prompts and dataset prompts using SBERT.
- Computes cosine similarity to find the top `n` most similar prompts.
- Provides a FastAPI-based API for programmatic access.
- Includes a user-friendly interface built with Streamlit.
