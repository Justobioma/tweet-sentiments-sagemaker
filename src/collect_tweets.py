import tweepy
import json
import time

def safe_search(client, query, max_results=100):
    for attempt in range(5):
        try:
            return client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=["created_at", "text", "author_id"])
        except tweepy.errors.TwitterServerError as e:
            print(f"Attempt {attempt+1}: Server error. Retrying in {2**attempt} seconds...")
            time.sleep(2**attempt)
    raise Exception("Twitter API failed after multiple retries.")



# Replace with your actual credentials
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAP3Y4AEAAAAANUC4Ou8N1Q%2B4tFSUd6q0e1dLARs%"

# Initialize client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Define search query
# query = "#Naija OR #EndSARS OR #Japa OR Nigeria lang:en -is:retweet"

query = "#Naija lang:en -is:retweet"


# Fetch tweets
response = client.search_recent_tweets(query=query, max_results=20, tweet_fields=["created_at", "text", "author_id"])

# Save tweets to JSON
tweets_data = []
for tweet in response.data:
    tweets_data.append({
        "id": tweet.id,
        "text": tweet.text,
        "author_id": tweet.author_id,
        "created_at": tweet.created_at.isoformat()
    })

with open("nigerian_tweets.json", "w", encoding="utf-8") as f:
    json.dump(tweets_data, f, ensure_ascii=False, indent=4)

print(f"Saved {len(tweets_data)} tweets to nigerian_tweets.json")