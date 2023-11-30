from flask import Flask
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

app = Flask(__name__)

cluster = MongoClient("")
db = cluster["nursery"]
collection = db["seeds"]

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/seeds", methods=["GET"])
def get_seeds():
    all_seeds = list(collection.find({}))
    return json.dumps(all_seeds, default=json_util.default)
