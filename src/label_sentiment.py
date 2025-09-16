import pandas as pd
import boto3
import time

# Load cleaned tweets
df = pd.read_csv("cleaned_tweets.csv")

# Initialize Comprehend client
comprehend = boto3.client("comprehend", region_name="eu-west-1")  # or your preferred region

# Function to get sentiment
def get_sentiment(text):
    try:
        response = comprehend.detect_sentiment(Text=text, LanguageCode="en")
        return response["Sentiment"]
    except Exception as e:
        print(f"Error: {e}")
        return "UNKNOWN"

# Apply sentiment detection
df["sentiment"] = df["clean_text"].apply(lambda x: get_sentiment(x) if isinstance(x, str) and len(x) > 0 else "UNKNOWN")

# Save labeled data
df.to_csv("labeled_tweets.csv", index=False, encoding="utf-8")
print("Sentiment labeling complete. Saved to labeled_tweets.csv")