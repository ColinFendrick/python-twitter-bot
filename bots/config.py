import logging
import os
import tweepy
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as err:
        logger.error("Error creating API", exc_info=True)
        raise err
    logger.info("API created")
    return api
