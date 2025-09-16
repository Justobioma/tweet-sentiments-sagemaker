# 🇳🇬 Nigerian Twitter Sentiment Analysis

This project analyzes the sentiment of tweets from Nigeria using NLP and AWS services.

## 🚀 Features
- Collect tweets using Twitter API
- Preprocess and clean text data
- Train sentiment classification model
- Deploy model using Amazon SageMaker
- Visualize results with Amazon QuickSight

## 🛠️ Tech Stack
- Python, Tweepy, scikit-learn
- AWS SageMaker, Lambda, S3, Comprehend
- Jupyter Notebooks, GitHub

## 📦 Setup
1. Clone repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Twitter API keys
4. Run `src/collect_tweets.py`

## 🧹 Preprocessing
Run `src/preprocess_tweets.py` to clean raw tweets and save them as `cleaned_tweets.csv`. This step removes noise and prepares the data for sentiment classification.

## 🧠 Sentiment Labeling
Run `src/label_sentiment.py` to auto-label tweets using Amazon Comprehend. This step adds a `sentiment` column to the dataset for training and analysis.

## 📊 Sample Output
![Sentiment Dashboard Screenshot](link-to-image-if-available)

## 📄 License
MIT License
