# Text-Image Search using Qdrant

## Introduction

This project demonstrates a text-to-image search system using Qdrant, enabling efficient similarity searches based on image captions on E-commerce based images. The system preprocesses data, computes embeddings, sets up Qdrant, and provides a search functionality through a Streamlit application.

## Files

1. **requirements.txt**: Contains the necessary Python packages and their versions for running the project.

2. **main.ipynb**: A Jupyter notebook that encompasses the following steps:
   - Data downloading
   - Preprocessing, including image caption generation using Blip
   - Data exploration
   - Embedding computation
   - Qdrant setup
   - Search functionality implementation

3. **main.py**: A Python script responsible for creating a Streamlit application to showcase the search results.

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/muhammad-usama-aleem/text-image-search-using-Qdrant.git
   ```
2. Navigate to the project directory::
  ```bash
  cd text-image-search-using-Qdrant
  ```

## Running the System

1. **Dependency Installation:**
    - Install the dependency using:
    ```bash
    pip install -r requirements.txt
    ```

2. **Notebook Execution:**
    - Open and execute the `main.ipynb` notebook using Jupyter or any compatible environment to perform the necessary steps.
  
3. **Streamlit Application:**
    - Run the following command to launch the Streamlit application:
      ```bash
      streamlit run main.py
      ```
    - Access the application in your web browser at [http://localhost:8501](http://localhost:8501).
    - NOTE: make sure to completely run the `main.ipynb` and store the data in Qdrant Vector DB

4. **Text-to-Image Searches:**
    - Utilize the Streamlit application to seamlessly perform text-to-image searches based on the embedded data.

5. **Visualization:**
    - Explore and visualize the search results interactively through the user-friendly interface.


## **System's Architecture:**

1. Used the following dataset for images:
  ```bash
  https://storage.googleapis.com/qdrant-examples/amazon-product-dataset-2020.zip
  ```

2. Used Image Captioning Model [Blip](https://huggingface.co/tasks/image-to-text#:~:text=Image%20to%20text%20models%20output,applications%20of%20image%20to%20text.) to get captions of the images.
3. For Embedding, I used [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). all-MiniLM-L6-v2: This is a sentence-transformers model: It maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search.
4. For Storing Embeddings and Similarity Search: I used [Qdrant](https://qdrant.tech/)


## Challenges Encountered:

1. E-commerce Dataset used didn't had captions. The descriptions could be used as captions but description of product were more like advertisements, so I had to discard the approcah.
