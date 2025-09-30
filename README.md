# 🇳🇬 Nigerian Twitter Sentiment Analysis

This project analyzes the sentiment of tweets from Nigeria using NLP and AWS services.

## 🚀 Features
- Collect tweets using Twitter API
- Preprocess and clean text data
- Train sentiment classification model
- Deploy model using Amazon SageMaker
  
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

## ✅ Achievements
1. Data Preparation
- Cleaned and normalized tweet data
- Filtered out nulls, empty strings, and irrelevant sentiment labels
- Mapped sentiment labels to binary format
2. Feature Engineering
- Used CountVectorizer with bigrams to capture expressive phrases like “no light”, “fuel price”, “we go make am”
- Fitted vectorizer on curated text samples
3. Model Training
- Trained an XGBoost binary classifier using DMatrix
- Tuned parameters for balanced performance
- Saved model using .save_model() for deployment compatibility
4. Evaluation
- Created a balanced test set of handcrafted Nigerian tweets
- Verified model predictions and adjusted threshold for better accurac
5. Deployment Preparation
- Built a custom inference.py script for SageMaker
- Packaged model, vectorizer, and script into model.tar.gz
- Uploaded to S3 for deployment
  
## ⚠️ Challenges
❌ SageMaker Container Compatibility
- Initial deployment failed due to missing MODEL_DIR environment variable
- Adjusted paths to /opt/ml/model/ to match container expectations
❌ Model Format Errors
- Despite using .save_model(), SageMaker’s XGBoost container rejected the file
- Tried multiple image versions (1.5-1, latest) with persistent errors
❌ Container Expectations
- Discovered SageMaker containers may expect models trained using their Estimator API
- Considered pivoting to SKLearn container or custom Docker image for flexibility
  
## 🧭 Next Steps
- Retrain using SageMaker’s built-in Estimator for full compatibility
- Explore custom container deployment for greater control
- Expand training data with more expressive negative samples
- Integrate endpoint into a real-time tweet stream or dashboard

## 🙌 Acknowledgments
Special thanks to the Nigerian tech community and open-source contributors whose tools and insights made this project possible.

## 📊 Sample Output
![Screenshot_26-9-2025_133445_eu-west-1 console aws amazon com](https://github.com/user-attachments/assets/a9b3ecba-7ccb-4496-a531-e135145d81f0)

![Screenshot_17-9-2025_18376_dzd-d8ba0lz74r0a8m sagemaker eu-west-1 on aws](https://github.com/user-attachments/assets/b1b71d8f-f65a-40c8-af61-6f813426250d)

![Screenshot_17-9-2025_173729_dzd-d8ba0lz74r0a8m sagemaker eu-west-1 on aws](https://github.com/user-attachments/assets/bebcaa60-71dc-4bcc-9e97-8c45426281ed)


## 📄 License
MIT License
