import streamlit as st
import requests

# Define the backend API endpoint
API_URL = 'http://backend:8000/most_similar'  # Use 'backend' as the hostname in Docker network

st.title("Prompt Search Engine")

# Input form
query = st.text_input("Enter your prompt:")
n = st.number_input("Number of similar prompts to retrieve:", min_value=1, max_value=100, value=5, step=1)

if st.button("Search"):
    if query.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        # Send request to the backend API
        response = requests.post(API_URL, json={"query": query, "n": n})
        if response.status_code == 200:
            results = response.json()["results"]
            
            st.subheader("Top Similar Prompts:")
            for score, prompt in results:
                st.write(f"**Similarity Score:** {score:.4f}")
                st.write(f"**Prompt:** {prompt}")
                st.write("---")
        else:
            st.error(f"Error: {response.json()['detail']}")
