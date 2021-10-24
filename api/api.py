from flask import jsonify
from flask import Flask
from flask import request
from datetime import datetime
import os
import sys
import time
import threading

app = Flask(__name__)

import json    

def check_headers(data, headers):
    for header in headers:
        if header not in data:
            return False
    return True



def fulfil_request(data):
    """
    takes the input from the api call and then returns the data we are interested in
    We will create a helper method to check whether the data of interest is in CockroachDB and instead use that if possible
    (an if statement of sorts)
    """

    ## if data in cockroachdb, get that and return

    ## else get the data from the google maps api and return that
    ## make sure to add this data to cockroach db too!

    return None

## get all info 
@app.route(f'/api/v0/get_all', methods = ["GET"])
def add_queue():
    data = request.get_json()
    if check_headers(data, ["type"]):
        ## do thing
        return processed_data,200

#A json get request with {coordinates:(lat,lng), radius:float, type: library, building, all}
@app.route(f'/api/v0/get_near', methods = ["GET"])
def remove_queue():
    data = request.get_json()
    if check_headers(data, ["coordinates", "radius", "type", "building", "all"]):
        return data, 200
        #return the final data


@app.route(f'/api/v0/alive', methods = ["GET"])
def ping_api():
    return "I'm There!", 200


if __name__ =='__main__':
    # ref.on_snapshot(lambda x,y,z: firestore_update(x,y,z,datas))
    app.run(host="0.0.0.0")