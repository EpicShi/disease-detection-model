import requests
import numpy as np
from PIL import Image
import streamlit as st
import tensorflow as tf
from constants import *


use_local_api = False


def predict_class(image_path):
    model = tf.keras.models.load_model(MODEl_PATH)
    original_image = Image.open(image_path)

    preprocessed_image = original_image.resize((256, 256))
    preprocessed_image = np.array(preprocessed_image) / 255.0

    preds = model.predict(np.expand_dims(preprocessed_image, axis=0))
    labels = ["Healthy", "Powdery", "Rust"]

    preds_class = np.argmax(preds)
    preds_label = labels[preds_class]

    return preds_label, round(preds[0][preds_class], 2)


def predict_class_from_api(image_path):
    files = {"file": image_path}
    headers = {"accept": "application/json"}

    try:
        response = requests.post(API_URL, headers=headers, files=files)
        response.raise_for_status()
        result = response.json()

        return result

    except requests.exceptions.HTTPError as err:
        print(err)
        return "Error", 0.0


def main():
    st.write("<h1>Disease Detection using CNN</h1>", unsafe_allow_html=True)

    with st.sidebar:
        st.image("assets/logo.png")

        uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

        st.info("""
                # About
                This is a web app to predict the disease in a plant using Convolutional Neural Network (CNN).
                
                # Contact
                For inquiries, you can mail us [here](mailto:arpitsengar99@gmail.com).
                """)

    home_page = st.empty()
    home_page.write(FRONT_PAGE, unsafe_allow_html=True)

    display_image = st.empty()
    classifying_text = st.empty()
    button = st.empty()

    if uploaded_file is not None:
        home_page.empty()
        display_image.image(uploaded_file, width=450)

        predict_button = button.button("Predict", use_container_width=True)

        if predict_button and uploaded_file is not None:
            classifying_text.empty()
            button.empty()
            with st.spinner("Predicting..."):
                label = (
                    predict_class(uploaded_file)
                    if use_local_api
                    else predict_class_from_api(uploaded_file)
                )

            st.toast("Prediction Complete!")
            st.info(f"""
    ##### Predicted Class:
    {label}

    ##### Description: 
    {DISEASE_DESCRIPTION[label]}
            """)

        classifying_text.empty()


if __name__ == "__main__":
    main()
