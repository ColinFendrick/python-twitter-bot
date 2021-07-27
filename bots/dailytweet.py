import logging
import time
import tweepy
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def main():
    api = create_api()
