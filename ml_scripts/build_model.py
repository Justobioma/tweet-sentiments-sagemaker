from sklearn.feature_extraction.text import TfidfVectorizer
from xgboost import XGBClassifier
import joblib

# Sample training data
texts = [
    "Nigerian youth are thriving",
    "This country tire me",
    "Peter Obi is the best thing to happen to Nigeria",
    "Lagos traffic go wound person today"
]
labels = [1, 2, 1, 2]  # 1 = Positive, 2 = Negative

# Fit the vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train the model
model = XGBClassifier()
model.fit(X, labels)

# Bundle and save
bundle = {"model": model, "vectorizer": vectorizer}
joblib.dump(bundle, "model_bundle.pkl")