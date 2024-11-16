# Import libraries
import streamlit as st
from PIL import Image
from utils.config_loader import ConfigLoader
from model.vqr_model import Virtual_Question_Answering
from custom_logger.custom_logging import CustomLogger

# Create a custom logger for the Streamlit app
logger = CustomLogger.create_custom_logger("StreamlitAPP")

# Function to initialize the VQA model
def initialize_vqa(config_path="config.yaml"):
    # Load configuration from the specified config file
    config = ConfigLoader.config_loader(config_path)
    if not config:
        st.error("Failed to load configuration. Please check config.yaml.")
        logger.error("Failed to load configuration.")
        return None
    try:
        # Initialize and load the VQA model
        VQA = Virtual_Question_Answering()
        VQA.load_model()
        return VQA
    except Exception as e:
        st.error("Failed to load the VQA model.")
        logger.error(f"Error loading VQA model: {e}")
        return None

# Function to process the uploaded image
def process_uploaded_image(uploaded_file, vqa_model):
    if uploaded_file is None:
        return

    try:
        # Open the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_container_width=True)

        # Generate caption for the uploaded image
        with st.spinner("Generating caption..."):
            caption = vqa_model.predict_model(uploaded_file)
            if caption:
                st.success("Caption Generated:")
                st.write(caption)
                logger.info("Caption generated successfully.")
            else:
                st.error("Failed to generate caption.")
                logger.error("Failed to generate caption.")
    except Exception as e:
        st.error("An error occurred while processing the image.")
        logger.error(f"Error processing image: {e}")

# Function to run the Streamlit app
def run_streamlit_app():
    st.title("Virtual Question Answering - Image Captioning")
    st.write("Upload an image to generate a caption")

    # Initialize the VQA model
    vqa_model = initialize_vqa()
    if not vqa_model:
        return

    # File uploader to upload an image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    process_uploaded_image(uploaded_file, vqa_model)