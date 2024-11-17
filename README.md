# Generate Caption of Image Project

## **Project Overview**

The **Generate Caption of Image** project combines **Computer Vision** and **Natural Language Processing (NLP)** to generate descriptive captions for images. By leveraging pre-trained transformer models and modern deployment practices, this project delivers an efficient and scalable solution for image captioning.

---

## **Features**

- Generates detailed captions for images using pre-trained transformer models.
- Modularized codebase employing Object-Oriented Programming (OOP) principles.
- Comprehensive monitoring and logging for debugging and tracking execution.
- Dockerized environment for platform-independent deployment.
- Configurable and maintainable project structure.

---

## **Tools and Libraries Used**

1. **Programming Language**: Python
2. **Transformer Model**: `nlpconnect/vit-gpt2-image-captioning`
3. **Feature Extraction and Tokenization**: VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer.
4. **Logging**: Tracks execution steps.
5. **Configuration Management**: `config.yaml` for external variables.
6. **PyTorch (torch)**: Efficient GPU-based model execution.
7. **Environment Management**: `requirements.txt` for dependency tracking.
8. **Docker**: Encapsulates the application for deployment.
9. **Pillow (PIL)**: Handles image processing.
10. **Streamlit**: Provides a GUI for interaction.

---

## **Project Structure**

```plaintext
VIRTUAL_QUESTION_ANSWERING_PROJECT/
│
├── main.py                    # Entry point of the application
├── DockerFile                 # Docker configuration for deployment
├── config.yaml                # Stores configurable variables
│
├── custom_logger              # Handles logging functionalities
│      ├── __init__.py
│      └── custom_logging.py
│
├── utils                      # Utility functions and configuration loader
│      ├── __init__.py
│      └── config_loader.py
│
├── model                      # Core model and experiment files
│      ├── __init__.py
│      ├── vqa_experiment.ipynb
│      └── vqr_model.py
│
└── application                # GUI using Streamlit
         ├── __init__.py
         └── streamlit.py
```

---

## **How to Run**

### 1. **Setup Environment**

- Create and activate a virtual environment:

  ```bash
  python -m venv env
  source env/bin/activate  # On Windows: env\Scripts\activate
  ```

- Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

### 2. **Run the Application**

- Launch the Streamlit app:

  ```bash
  streamlit run application/streamlit.py
  ```

---

## **Docker Setup**

### 1. **Build Docker Image**

- Run the following command to create the Docker image:

  ```bash
  docker build -t generate_caption .
  ```

### 2. **Run Docker Container**

- Start the container:

  ```bash
  docker run -p 8501:8501 generate_caption
  ```

### 3. **Access the Application**

- Open your browser and navigate to:

  ```bash
  http://localhost:8501
  ```

---

## **GPU Setup**

1. Install the **NVIDIA Container Toolkit** to enable GPU support in Docker.  
   Follow the [NVIDIA documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) to set it up.

2. Modify the `docker run` command to utilize the GPU:

   ```bash
   docker run --gpus all -p 8501:8501 generate_caption
   ```

3. Ensure `torch` is configured for GPU by checking:

   ```python
   import torch
   print(torch.cuda.is_available())  # Should return True
   ```

---

## **Future Enhancements**

1. **Advanced Models**: Explore other models for enhanced captioning accuracy.  
2. **Multilingual Support**: Extend the application to generate captions in multiple languages.  
3. **Image Editing Features**: Allow users to edit and manipulate images before captioning.  
4. **Cloud Deployment**: Deploy the application to cloud platforms like AWS, Azure, or GCP for wider accessibility.  
5. **Mobile Application**: Develop a mobile app interface for on-the-go captioning.

---

## **Contributors**

- **Fathy Hesham Fathy**  
  - Machine Learning and NLP Developer  
  - [GitHub](https://github.com/FathyHesham) | [LinkedIn](https://www.linkedin.com/in/fathy-hesham-fathy/)

To resolve the **MD047/single-trailing-newline** warning, simply add a blank line at the end of the file. Here's the updated **License** section with a newline at the end:

---

## **License**

- This project is licensed under the **MIT License**.
