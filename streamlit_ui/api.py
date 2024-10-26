import streamlit as st
import requests

# Define the backend API endpoint
API_URL = 'http://localhost:8000/search' 

st.set_page_config(page_title="Promp search engine")
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
            results = response.json()
            if results:
                    st.success(f"Top {n} similar prompts:")
                    for idx, result in enumerate(results, start=1):
                        similarity = result["similarity_score"]
                        prompt = result["prompt"]
                        st.write(f"**{idx}. Prompt:** {prompt}")
                        st.write(f"**Similarity Score:** {similarity:.4f}")
                        st.write("---")
            else:
                    st.info("No similar prompts found.")
        else:
            st.error(f"Error: {response.json()['detail']}")