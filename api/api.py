from psycopg2.errors import SerializationFailure
from flask import jsonify
from flask import Flask
from flask import request
from datetime import datetime
import os
import sys
import time
import threading
import populartimes
import psycopg2
import urllib

import sched
s = sched.scheduler(time.time, time.sleep)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction

from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

app = Flask(__name__)


import json   

def read_libraries(filename="libraries.json"):
    with open(filename,"r") as f:
        libraries = json.loads(f.read())
    return libraries

libraries = read_libraries()
cache = {}

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
    #cockroach_data, http_code = fulfill_request_helper("SELECT * FROM ____", conn)
    for library in libraries:
        data = populartimes.get_id(api_key, library)
        print(libraries[library], data.get("current_popularity"))
        cockroach_data, http_code = fulfill_request_helper("INSERT INTO location_data ${} VALUES ${}", conn)
    if http_code != 404:
        return cockroach_data
    else:
        ## else get the data from the google maps api and return that
        ## make sure to add this data to cockroach db too!
        return None

## get all info 
@app.route(f'/api/v0/get_all', methods = ["GET"])
def add_queue():
    data = request.get_json()
    print(api_key)
    if check_headers(data, ["type"]):
        ## do thing
        fulfil_request(data)
        return "",200

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

def back_run(conn):
    libraries = read_libraries()
    columns = ['id', 'type', 'popularity', 'name', 'loc_point', 'last_time_updated', 'url', 'popular_times']
    temp_cache = []
    for library in libraries:
        with conn.cursor() as cur:
            data = populartimes.get_id(api_key, library)
            
            sql_statement = f'INSERT INTO location_data ({", ".join(columns)}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            variables =  (library, "library", data.get("current_popularity",0), libraries.get(library), 
                f'({data.get("coordinates").get("lat")},{data.get("coordinates").get("lng")})', datetime.utcnow(), 
                f'https://www.google.com/maps/place/?q=place_id:{library}', json.dumps(data.get("populartimes", [])))
            cur.execute(sql_statement, variables)
            # print(f'delete_accounts(): status message: {cur.statusmessage}')
            library_cache = {}
            for k,v in zip(columns, variables):
                library_cache[k] = v
            print(library_cache)
            temp_cache.append(library_cache)
    cache = temp_cache
    conn.commit()

if __name__ =='__main__':
    # ref.on_snapshot(lambda x,y,z: firestore_update(x,y,z,datas))
    try:
        # engine = create_engine(os.getenv("DB_CONN"))
        conn_str = f'{os.getenv("DB_CONN").strip("")}?sslmode=verify-full&sslrootcert=$HOME/.postgresql/root.crt'
        conn_str =  urllib.parse.unquote(os.path.expandvars(conn_str))
        print(conn_str)
        conn = psycopg2.connect(conn_str)
        # print(fulfill_request_helper("SELECT * FROM location_data",conn))
    except Exception as e:
        print('Failed to connect to database.')
        print('{0}'.format(e))

            #cockroach_data, http_code = fulfill_request_helper(sql_statement, conn)

    
    back_run(conn)
    app.run(host="0.0.0.0")
    # def fulfill_request_helper(sql_statement, conn):

    # with conn.cursor() as cur:
        
    #     rows = cur.fetchall()
    #     if rows:
    #         return rows, 200
    #     else:
    #         return rows, 404