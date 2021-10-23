from flask import jsonify
from flask import Flask
from flask import request
from datetime import datetime
import os
import sys
import time
import threading

app = Flask(__name__)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
cred = credentials.Certificate('keys/creds.json')
firebase_admin.initialize_app(cred)
firestore_db = firestore.client()
# callback_done = threading.Event()
# ref = firestore_db.collection(u'users')
import json

def get_user_id(request):
    try:
        token = request.headers.get("User-Token")
        uid = auth.verify_id_token(token)['uid'] if token else None
        return uid
    except:
        return None
    
        

## all queue items take the following in the 
@app.route(f'/api/v0/add_queue_item', methods = ["GET"])
def add_queue():
    uid = get_user_id(request)
    if uid:
        del uid


@app.route(f'/api/v0/remove_queue_item', methods = ["GET"])
def remove_queue():
    uid = get_user_id(request)

@app.route(f'/api/v0/decouple_item', methods = ["GET"])
def decouple_request():
    uid = get_user_id(request)


@app.route(f'/api/v0/alive', methods = ["GET"])
def ping_api():
    return "I'm There!", 200


if __name__ =='__main__':
    # ref.on_snapshot(lambda x,y,z: firestore_update(x,y,z,datas))
    app.run(host="0.0.0.0")