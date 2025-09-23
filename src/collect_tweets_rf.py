import tweepy
import json
import time
import logging
from datetime import datetime

# ---------------------- CONFIGURATION ---------------------- #
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAP3Y4AEAAAAAJsRmj9%2FSao3QAcTytfpdipTT5%2BI%3DRy3uGBdDZDyIiYUrzlL7H1iojg66fIx0R7wGCDuo3nzbcp2pzi"
QUERY ="Lagos lang:en -is:retweet"
MAX_RESULTS = 50  # Reduce if hitting errors
OUTPUT_FILE = f"nigerian_tweets_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
MAX_ATTEMPTS = 5

# ---------------------- LOGGING SETUP ---------------------- #
logging.basicConfig(
    filename="tweet_collection.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------------- TWITTER CLIENT ---------------------- #
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# ---------------------- FETCH FUNCTION ---------------------- #
def fetch_tweets(query, max_results):
    for attempt in range(MAX_ATTEMPTS):
        try:
            logging.info(f"Attempt {attempt+1}: Fetching tweets...")
            response = client.search_recent_tweets(
                query=query,
                max_results=max_results,
                tweet_fields=["created_at", "text", "author_id"]
            )
            return response.data
        except tweepy.errors.TwitterServerError as e:
            wait_time = 2 ** attempt
            logging.warning(f"Server error: {e}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            break
    logging.error("Failed to fetch tweets after multiple attempts.")
    return []

# ---------------------- MAIN EXECUTION ---------------------- #
def main():
    tweets = fetch_tweets(QUERY, MAX_RESULTS)
    if not tweets:
        print("No tweets collected.")
        return

    tweets_data = []
    for tweet in tweets:
        tweets_data.append({
            "id": tweet.id,
            "text": tweet.text,
            "author_id": tweet.author_id,
            "created_at": tweet.created_at.isoformat()
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(tweets_data, f, ensure_ascii=False, indent=4)

    print(f"✅ Collected {len(tweets_data)} tweets. Saved to {OUTPUT_FILE}")
    logging.info(f"Successfully saved {len(tweets_data)} tweets to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()