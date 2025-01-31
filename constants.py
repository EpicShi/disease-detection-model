MODEl_PATH = "weights/plant_disease_classifier.h5"
FRONT_PAGE = """
<body style="font-family: Arial, sans-serif; color: #333; font-size: 16px;">
    <p>Welcome to the "Disease Detection using CNN" Streamlit web application. This tool is designed to assist you in identifying the health status of your plants with the help of a Convolutional Neural Network (CNN).</p>
    <h2>Get Started</h2>
    <p>To begin using this application, follow these steps:</p>
    <ol>
        <li>Click the "Upload an Image" button in the sidebar.</li>
        <li>Select an image of your plant from your device.</li>
        <li>Click the "Predict" button to see the classification result.</li>
    </ol>
    <h2>About</h2>
    <p>This web application is built using Streamlit and powered by a deep learning model. It offers a user-friendly interface for Disease detection, making it accessible to anyone interested in plant health.</p>
</body>
"""

DISEASE_DESCRIPTION = {
    "Healthy": "Your plant appears to be healthy! Keep up the good work with your plant care routine to maintain its health and vitality. Regular watering, proper sunlight exposure, and monitoring for pests and diseases can help your plant thrive.",
    "Powdery": "Powdery mildew is a fungal disease that affects a wide range of plants, including fruits, vegetables, and ornamental plants. It appears as a white or gray powdery growth on the leaves, stems, and flowers of infected plants. Powdery mildew can weaken the plant, reduce fruit yield, and affect the overall health of the plant. It is important to treat powdery mildew early to prevent its spread and protect the plant from further damage.",
    "Rust": "Rust is a common Disease caused by various fungi. It appears as orange, yellow, or reddish-brown pustules on the leaves, stems, or fruit of infected plants. Rust can weaken the plant, reduce photosynthesis, and affect the overall health of the plant. It is important to treat rust early to prevent its spread and protect the plant from further damage.",
}

API_URL = "https://arpy8-drishti-api.hf.space/predict"
