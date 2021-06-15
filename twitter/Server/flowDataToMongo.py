import pymongo
from bson.json_util import dumps
import json
from flask import Flask, request, render_template, session, redirect, g,url_for, flash, Response, abort, render_template_string, send_from_directory
from flask_cors import CORS
from PIL import Image
from io import StringIO
import time
import base64
import requests
import random

app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = b'\xd2(*K\xa0\xa8\x13]g\x1e9\x88\x10\xb0\xe0\xcc'

#Loads the Database and Collections
mongo = pymongo.MongoClient("mongodb+srv://vishwajeet:Mjklop@cluster0.pkcgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = mongo["twitterStream"]

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Enter Twitter API Keys
access_token = "1380563468495904769-XyEXZ8RR6NZDKwzuN11KDzJcvx14cV"
access_token_secret = "0khUTnzK2crKZrUDVKgkF6D1Un5B0lAfPkVIP4Hp6qKrx"
consumer_key = "f4DyH3YGd58RCc6qDkSiCxdhK"
consumer_secret = "bqVsAXoYAUzf6T7qG6ra2TTCM0rmEiNuaBDNwDEgoHQHWcN1gE"
class StdOutListener(StreamListener):
        
        def on_data(self, data):   
            # print(type(data))
            tweet = json.loads(data)
            twitter_data = pymongo.collection.Collection(db, 'twitter')
            twitter_data.insert_one(tweet)
            time.sleep(1)
            print(tweet["text"])
            return True
            

        def on_error(self, status):
            print(status)
app.route("/")
def get_data():
    
    return {"All tweets are being heard here"}
app.route("/fetch_new",methods=["GET"])
def get_recent_data():
    twitter_data = pymongo.collection.Collection(db, 'twitter')
    all1 = twitter_data.find().sort({id:1})
    return all1
if __name__ == '__main__':  
# Handle Twitter authetification and the connection to Twitter Streaming API
    
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    tracklist = ["Transfer news football"]
    stream.filter(track=tracklist)
