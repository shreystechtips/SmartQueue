from psycopg2.errors import SerializationFailure
from flask import jsonify
from flask import Flask
from flask import request
from datetime import datetime, timedelta
import os
import sys
import time
import threading
import populartimes
import psycopg2
import urllib

import geopy
import sched
s = sched.scheduler(time.time, time.sleep)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction

from flask_cors import CORS

from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")


app = Flask(__name__)
cors = CORS(app)

import json   

def read_libraries(filename="libraries.json"):
    with open(filename,"r") as f:
        libraries = json.loads(f.read())
    return libraries

libraries = read_libraries()
cache = []
conn = None

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
    global cache
    
    sorted_values = cache
    if "radius" and "coordinates" in data:
        temp = []
        for x in sorted_values:
            location = tuple(float(val.strip("()")) for val in x['loc_point'].split(","))
            
            if geopy.distance.distance(location, data["coordinates"]).miles < data['radius']:
                x['distance'] = geopy.distance.distance(location, data["coordinates"]).miles
                temp.append(x)
        sorted_values = sorted([x for x in temp], 
                        key= lambda x: (geopy.distance.distance(location, data["coordinates"]).miles, x['popularity']), reverse = True)
        #
    else:
        for i in range(len(sorted_values)):
            sorted_values[i]['distance'] = 0
            
    return {'ret': sorted_values}

    

## get all info 
@app.route(f'/api/v0/get_all', methods = ["POST"])
def add_queue():
    data = request.get_json()
    if check_headers(data, ["type"]):
        ## do thing
        return fulfil_request(data),200
    return "bad request", 404

#A json get request with {coordinates:(lat,lng), radius:float, type: library, building, all}
@app.route(f'/api/v0/get_near', methods = ["POST"])
def remove_queue():
    data = request.get_json()
    if check_headers(data, ["coordinates", "radius","type"]):
        return fulfil_request(data),200
        #return the final data
    return "bad request", 404


@app.route(f'/api/v0/alive', methods = ["GET"])
def ping_api():
    return "I'm There!", 200

def get_key_time(key, cur):
    cur.execute("SELECT * FROM location_data WHERE id LIKE %s", (key,))
    return cur.fetchone()



@app.route(f'/api/v0/update', methods = ["GET"])
def update():
   back_run(conn) 
   return "",200

last_updated = None

def back_run(conn = conn, time_diff = timedelta(minutes = 21)):
    global cache
    global last_updated
    
    if last_updated and datetime.now() - last_updated <= timedelta(minutes = 5):
        return

    libraries = read_libraries()
    columns = ['id', 'type', 'popularity', 'name', 'loc_point', 'last_time_updated', 'url', 'popular_times']
    temp_cache = []
    for library in libraries:
        with conn.cursor() as cur:
            data = populartimes.get_id(api_key, library)
            db_data = get_key_time(library, cur)
            if db_data:
                updated_time = db_data[5]
            if not db_data or datetime.utcnow() - updated_time >= time_diff:

                if not db_data:
                    print("no data")
                    sql_statement = f'INSERT INTO location_data ({", ".join(columns)}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                    data =  (library, "library", data.get("current_popularity",0), libraries.get(library), 
                        f'({data.get("coordinates").get("lat")},{data.get("coordinates").get("lng")})', datetime.utcnow(), 
                        f'https://www.google.com/maps/place/?q=place_id:{library}', json.dumps(data.get("populartimes", [])))
                else:
                    print("data")
                    sql_statement = f'UPDATE location_data SET {", ".join([x+" = %s" for x in columns if not x == "id"])} WHERE id = %s'
                    data = ("library", data.get("current_popularity",0), libraries.get(library), 
                        f'({data.get("coordinates").get("lat")},{data.get("coordinates").get("lng")})', datetime.utcnow(), 
                        f'https://www.google.com/maps/place/?q=place_id:{library}', json.dumps(data.get("populartimes", [])), library)
                
                cur.execute(sql_statement, data)

            if data:
                library_cache = {}
                for k,v in zip(columns, db_data):
                    library_cache[k] = v
                
                library_cache["popular_times"] = json.loads(library_cache["popular_times"] )
                temp_cache.append(library_cache)

    cache = sorted([x for x in temp_cache], key=  lambda x: x['popularity'])

    conn.commit()
    last_updated = datetime.now()

try:

    conn_str = f'{os.getenv("DB_CONN").strip("")}?sslmode=verify-full&sslrootcert=./root.crt'
    conn_str =  urllib.parse.unquote(os.path.expandvars(conn_str))
    # print(conn_str)
    conn = psycopg2.connect(conn_str)
except Exception as e:
    print('Failed to connect to database.')
    print('{0}'.format(e))

back_run(conn)
if __name__ =='__main__':
    app.run(host="0.0.0.0")
