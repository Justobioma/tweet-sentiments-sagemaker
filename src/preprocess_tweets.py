import json
import pandas as pd
import re
import emoji
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load raw tweet data
with open("nigerian_tweets.json", "r", encoding="utf-8") as f:
    raw_tweets = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(raw_tweets)

# Define cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # Remove URLs
    text = re.sub(r"@\w+", "", text)  # Remove mentions
    text = re.sub(r"#", "", text)  # Remove hashtag symbol
    text = emoji.replace_emoji(text, replace='')  # Remove emojis
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    return " ".join(tokens)

# Apply cleaning
df["clean_text"] = df["text"].apply(clean_text)

# Save cleaned data
df.to_csv("cleaned_tweets.csv", index=False, encoding="utf-8")
print(f"Saved cleaned tweets to cleaned_tweets.csv")