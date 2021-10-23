from flask import jsonify
from flask import Flask
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
cred = credentials.Certificate('creds.json')
firebase_admin.initialize_app(cred)
firestore_db = firestore.client()
callback_done = threading.Event()
ref = firestore_db.collection(u'users')
import json