import tweepy
import json

# Replace with your actual credentials
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAP3Y4AEAAAAANUC4Ou8N1Q%2B4tFSUd6q0e1dLARs%"

# Initialize client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Define search query
query = "#Naija OR #EndSARS OR #Japa OR Nigeria lang:en -is:retweet"

# Fetch tweets
response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["created_at", "text", "author_id"])

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