import xgboost as xgb
import joblib

model = xgb.XGBClassifier()
model.load_model("xgb_model.json")

vectorizer = joblib.load("vectorizer.pkl")
features = vectorizer.transform(["Naija youths dey hustle"]).toarray()
prediction = model.predict(features)
print("Prediction:", prediction)