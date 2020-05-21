from twitterscraper.query import query_user_info
from twitterscraper import query_tweets
import datetime as dt
global twitter_user_info


def get_user_info(twitter_user):
    """
    An example of using the query_user_info method
    :param twitter_user: the twitter user to capture user data
    :return: twitter_user_data: returns a dictionary of twitter user data
    """
    user_info = query_user_info(user=twitter_user)
    twitter_user_data = {}
    twitter_user_data["user"] = user_info.user
    twitter_user_data["fullname"] = user_info.full_name
    twitter_user_data["location"] = user_info.location
    twitter_user_data["blog"] = user_info.blog
    twitter_user_data["date_joined"] = user_info.date_joined
    twitter_user_data["id"] = user_info.id
    twitter_user_data["num_tweets"] = user_info.tweets
    twitter_user_data["following"] = user_info.following
    twitter_user_data["followers"] = user_info.followers
    twitter_user_data["likes"] = user_info.likes
    twitter_user_data["lists"] = user_info.lists
    print(user_info.tweets)
    return twitter_user_data


def load_tweets(d, m, y):
    flat_tweets = query_tweets("Romania coronavirus", 10, dt.date(y, m, d))

    tweets = []

    for tweet in flat_tweets:
        tweets_obj = {
            'id': tweet.tweet_id,
            'text': tweet.text,
            'html': tweet.text_html,
            'url': tweet.tweet_url,
            'user': tweet.username,
            'time': tweet.timestamp
        }
        tweets.append(tweets_obj)

    return tweets