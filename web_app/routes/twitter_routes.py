

from flask import Blueprint, jsonify #, render_template, request , flash, redirect
from web_app.services.twitter_service import api as twitter_api

#from web_app.models import db, Book, parse_records

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user_data(screen_name):
    print("FETCHING:", screen_name)
    
    #TO DO: fetch user info
    user = twitter_api.get_user(screen_name)
    
    #TO DO: fetch their tweets
    statuses = twitter_api.user_timeline(screen_name, tweet_mode="extended", count=35, exclude_replies=True, include_rts=False)
    
    #TO DO: fetch embedding for their tweet
    
    #TO DO: store their tweets in database (with embeding)
    
    
    #return f"FETCHED {screen_name} OK"
    return jsonify({"user": user._json, "num_of_tweets": len(statuses)})