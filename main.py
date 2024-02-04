import streamlit as st
from PIL import Image
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

try:
    client = QdrantClient("localhost")
    collections = client.get_collections()
except Exception:
    client = QdrantClient(":memory:")
    collections = client.get_collections()


encoder = SentenceTransformer("all-MiniLM-L6-v2")


def get_response(user_prompt):
    
    hits = client.search(
        collection_name="E-commerce",
        query_vector=encoder.encode(str(user_prompt)).tolist(),
        limit=3,
    )
    result_image = []
    for hit in hits:
        result_image.append((hit.payload['LocalImage'], hit.payload['caption']))
    return result_image


def main():
    st.title("Text to Image App")

    user_prompt = st.text_area("Enter text:")

    if st.button("Generate Images") and user_prompt != '':
        processed_data = get_response(user_prompt)

        if processed_data:
            num_columns = len(processed_data)
            columns = st.columns(num_columns)
            for i, (image, caption) in enumerate(processed_data):
                columns[i].image(image, caption=caption, use_column_width=True)
        else:
            st.warning("No matching images found. Try a different prompt.")
    else:
        st.warning("You forgot to write something.")

if __name__ == "__main__":
    main()
