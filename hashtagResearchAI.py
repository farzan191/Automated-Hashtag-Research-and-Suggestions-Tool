import tweepy
import pandas as pd

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_secret = 'your_access_secret'

# Set up Tweepy with credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

def get_trending_hashtags(location_id, num_hashtags):
    """
    Fetch trending hashtags for a given location.

    Parameters:
    - location_id: Twitter WOEID (Where On Earth ID) for the desired location.
    - num_hashtags: Number of trending hashtags to retrieve.

    Returns:
    - List of trending hashtags.
    """
    try:
        trending = api.trends_place(id=location_id, exclude='hashtags')[0]['trends']
        trending_hashtags = [trend['name'] for trend in trending[:num_hashtags]]
        return trending_hashtags
    except tweepy.TweepError as e:
        print(f"Error fetching trending hashtags: {e}")
        return []

def suggest_hashtags(text, num_suggestions):
    """
    Analyze text and suggest relevant hashtags.

    Parameters:
    - text: Text of the post or content.
    - num_suggestions: Number of hashtag suggestions to generate.

    Returns:
    - List of suggested hashtags.
    """
    # Simplified logic: Extract words starting with '#'
    words_with_hashtags = [word[1:] for word in text.split() if word.startswith('#')]
    return words_with_hashtags[:num_suggestions]

# Example usage
location_woeid = 1  # WOEID for worldwide trends
num_trending_hashtags = 5
num_hashtag_suggestions = 3

# Fetch trending hashtags
trending_hashtags = get_trending_hashtags(location_woeid, num_trending_hashtags)
print(f"Trending Hashtags: {trending_hashtags}")

# Example post text
post_text = "Exciting times ahead! Ready for the weekend. #FridayFeeling"

# Suggest hashtags based on the post text
suggested_hashtags = suggest_hashtags(post_text, num_hashtag_suggestions)
print(f"Suggested Hashtags: {suggested_hashtags}")
