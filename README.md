# Disease Detection Model

This repository contains the source code and training notebook for the plant disease detection model. The directory also contains a simple web app for testing purposes, allowing users to upload a sample image of a plant and the CNN model predicts whether the plant is healthy or if it is affected by powdery, mildew or rusty. 

---

### Important Links:

Model Weights:
	- [https://www.mediafire.com/file/1j3dwd2pzs7xc13/weights.rar/file](https://www.mediafire.com/file/1j3dwd2pzs7xc13/weights.rar/file).

---

## Usage
1. Download and place the model weights file (`plant_disease_classifier.h5`) in the `weights` directory. (optional)

2. Install the required packages using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

4. The web app will open in your default web browser, allowing you to upload plant images for disease classification.

## File Structure

```
├── README.md
├── assets/
├── weights/
├── constants.py
├── main.py
└── requirements.txt
```

## Model

The model used for Disease classification is a CNN model. It has been trained to classify plants into one of the following categories:
- Healthy
- Powdery
- Rust
