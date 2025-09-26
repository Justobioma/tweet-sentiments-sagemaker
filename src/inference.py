import os
import pickle
import numpy as np
import xgboost as xgb

def model_fn(model_dir):
    booster = xgb.Booster()
    booster.load_model(os.path.join(model_dir, "xgb_model.json"))

    with open(os.path.join(model_dir, "fitted_vectorizer.pkl"), "rb") as f:
        vectorizer = pickle.load(f)

    print("🧬 Loaded vocab size:", len(vectorizer.vocabulary_))
    print("🧬 Loaded IDF fingerprint:", getattr(vectorizer, "idf_", "Missing"))

    if not hasattr(vectorizer, "idf_"):
        raise RuntimeError("🚨 Vectorizer is not fitted!")

    return {"booster": booster, "vectorizer": vectorizer}


def input_fn(request_body, request_content_type):
    """Parse the incoming request body."""
    if request_content_type == "text/csv":
        return request_body.strip()
    raise ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_data, model_bundle):
    booster = model_bundle["booster"]
    vectorizer = model_bundle["fitted_vectorizer"]

    features = vectorizer.transform([input_data])
    dmatrix = xgb.DMatrix(features)

    raw_pred = booster.predict(dmatrix)
    predicted_class = int(raw_pred[0] > 0.5)
    return [predicted_class]



# """ def output_fn(prediction, response_content_type):
#     """Format the prediction output."""
#     return str(prediction[0]) """

def output_fn(prediction, response_content_type):
    """Format the prediction output."""
    label_map = {0: "Negative", 1: "Positive"}  # fallback if not in bundle
    try:
        # If label_map is stored in the bundle
        label_map = bundle.get("label_map", label_map)
    except:
        pass

    label = label_map.get(int(prediction[0]), "Unknown")
    return label