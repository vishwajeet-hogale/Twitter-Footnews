import pymongo
from bson.json_util import dumps
import json
from flask import Flask, request, render_template, session, redirect, g,url_for, flash, Response, abort, render_template_string, send_from_directory
from flask_cors import CORS
from PIL import Image
from io import StringIO

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


#Home page
@app.route('/')
def home_page():
	return render_template('index.html')
@app.route("/fetch")
def fetch():
    all1 = []
    for i in db.twitter.find():
        i = dict(i)
        del i["_id"]
        all1.append(dict(i))
    print(all1)
    print(type(all1[0]))
    return {"data":all1}
	

	
	
if __name__=="__main__":
	app.run(debug=True)