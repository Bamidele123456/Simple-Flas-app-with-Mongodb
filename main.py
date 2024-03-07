from flask import Flask
import pymongo
from pymongo import MongoClient
import json
from bson import json_util
app = Flask(__name__)


cluster = MongoClient("")

db = cluster["nursery"]
collection = db["seeds"]

# post_1 = {"_id": 0, "seeds": "peas"}
# post_2 = {"_id": 1, "seeds": "apples"}
# post_3 = {"_id": 2, "seeds": "oranges"}
#
# collection.insert_many([post_1, post_2, post_3])

@app.route("/seeds", methods=["GET"])
def get_seeds():
    all_seeds = list(collection.find({}))
    return json.dumps(all_seeds, defaut=json_util.default)
