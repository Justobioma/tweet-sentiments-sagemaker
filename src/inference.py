import os
import joblib
import numpy as np
import xgboost as xgb

def model_fn(model_dir):
    """Load the XGBoost model and vectorizer from the model directory."""
    # Load XGBoost model
    model_path = os.path.join(model_dir, "xgb_model.json")
    model = xgb.XGBClassifier()
    model.load_model(model_path)

    # Load vectorizer
    vectorizer_path = os.path.join(model_dir, "vectorizer.pkl")
    vectorizer = joblib.load(vectorizer_path)




def input_fn(request_body, request_content_type):
    """Parse the incoming request body."""
    if request_content_type == "text/csv":
        return request_body.strip()
    raise ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_data, bundle):
    """Transform input text and make prediction."""
    vectorizer = bundle["vectorizer"]
    model = bundle["model"]

    # Transform the raw text into numeric features
    features = vectorizer.transform([input_data]).toarray()

    # Predict using the XGBoost model
    prediction = model.predict(features)
    return prediction

# """ def output_fn(prediction, response_content_type):
#     """Format the prediction output."""
#     return str(prediction[0]) """

def output_fn(prediction, response_content_type):
    """Format the prediction output."""
    label_map = {0: "Positive", 1: "Negative"}  # fallback if not in bundle
    try:
        # If label_map is stored in the bundle
        label_map = bundle.get("label_map", label_map)
    except:
        pass

    label = label_map.get(int(prediction[0]), "Unknown")
    return label