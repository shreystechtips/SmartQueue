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
    global cache
    
    sorted_values = cache

    if "radius" and "coordinates" in data:
        temp = []
        # sorted_values = sorted([cache[place_id] for place_id in cache], key: lambda x: (geopy.distance.distance(x['loc_point'], x['popularity']))
        for x in sorted_values:
            # x = sorted_values[place_id]
            # place_id = x['id']
            location = (float(val.strip("()")) for val in x['loc_point'].split(","))
            if geopy.distance.distance(location, data["coordinates"]).miles < data['radius']:
                temp.append(x)
        sorted_values = sorted([x for x in temp], 
                        key= lambda x: (geopy.distance.distance(location, data["coordinates"]).miles, x['popularity']))
                   
    return {'ret': sorted_values}

    

## get all info 
@app.route(f'/api/v0/get_all', methods = ["GET"])
def add_queue():
    data = request.get_json()
    print(api_key)
    if check_headers(data, ["type"]):
        ## do thing
        return fulfil_request(data),200
    return "bad request", 404

#A json get request with {coordinates:(lat,lng), radius:float, type: library, building, all}
@app.route(f'/api/v0/get_near', methods = ["GET"])
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
    print(key)
    cur.execute("SELECT * FROM location_data WHERE id LIKE %s", (key,))
    return cur.fetchone()

def back_run(conn, time_diff = timedelta(minutes = 10)):
    global cache

    # with open("test.json","r") as f:
    #     temp = json.loads(f.read())
    #     for x in temp:
    #         try:
    #             temp[x]['last_time_updated'] = datetime.datetime.strptime(temp[x]['last_time_updated'], "%Y-%m-%d %H:%M:%S")
    #         except:
    #             continue
    #     cache = temp
    #     # print(cache)
    # return

    libraries = read_libraries()
    columns = ['id', 'type', 'popularity', 'name', 'loc_point', 'last_time_updated', 'url', 'popular_times']
    temp_cache = {}
    for library in libraries:
        with conn.cursor() as cur:
            data = populartimes.get_id(api_key, library)
            db_data = get_key_time(library, cur)
            if db_data:
                updated_time = db_data[5]
            if not db_data or datetime.utcnow() - updated_time >= time_diff:
                print('hi')
                if db_data:
                    print(datetime.utcnow() - updated_time)
                print(data)
                sql_statement = f'INSERT INTO location_data ({", ".join(columns)}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                data =  (library, "library", data.get("current_popularity",0), libraries.get(library), 
                    f'({data.get("coordinates").get("lat")},{data.get("coordinates").get("lng")})', datetime.utcnow(), 
                    f'https://www.google.com/maps/place/?q=place_id:{library}', json.dumps(data.get("populartimes", [])))
                cur.execute(sql_statement, data)
                # print(f'delete_accounts(): status message: {cur.statusmessage}')
            if data:
                library_cache = {}
                for k,v in zip(columns, data):
                    library_cache[k] = v
                print(library_cache)
                temp_cache[library] = library_cache
    cache.update(temp_cache)
    cache = sorted([cache[place_id] for place_id in cache], key=  lambda x: x['popularity'])
    # with open("test.json","w") as f:
    #     f.write(json.dumps(cache, default=str))
    conn.commit()
    s.enter(60, 1, back_run, (conn,))


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

    print('hello2')
    s.enter(0, 1, back_run, (conn,))
    s.run()
    print('hello')
    # back_run(conn)

    app.run(host="0.0.0.0")
    # def fulfill_request_helper(sql_statement, conn):

    # with conn.cursor() as cur:
        
    #     rows = cur.fetchall()
    #     if rows:
    #         return rows, 200
    #     else:
    #         return rows, 404