import os
import joblib
import numpy as np

def model_fn(model_dir):
    """Load the model and vectorizer from the model directory."""
    bundle_path = os.path.join(model_dir, "model_bundle.pkl")
    bundle = joblib.load(bundle_path)
    return bundle

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

def output_fn(prediction, response_content_type):
    """Format the prediction output."""
    return str(prediction[0])