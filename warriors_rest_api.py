from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import pymongo
from bson.json_util import dumps
import json,sys
from flask_restful import Resource, Api
import math


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Warriors-SeeCow'
app.config['MONGO_URI'] = 'mongodb+srv://warriors:warriors@warriors-vc2w4.mongodb.net/test'

mongo = pymongo.MongoClient('mongodb+srv://warriors:warriors@warriors-vc2w4.mongodb.net/test', maxPoolSize=50, connect=False)

db = pymongo.database.Database(mongo,'Warriors-SeeCow')
CATTLE_STATUS = pymongo.collection.Collection(db,'CATTLE_STATUS')

mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Welcome to Warriors-SeeCow API'

@app.route('/current_status', methods=['GET'])
def current_status():
    return jsonify({'result' : json.loads(dumps(CATTLE_STATUS.find().limit(5).sort("time", -1)))})

@app.route('/cattle/<id>', methods=['GET'])
def get_one_cattle(id):

    q = CATTLE_STATUS.find_one({'CATTLE_ID' : id})

    if q:
        output = {'id' : q['CATTLE_ID'], 'Cattle Status' : q['Status']}
    else:
        output = 'No results found'

    return jsonify({'result' : output})

@app.route('/update_status/<id>/<Status>/<LOCATION>', methods=['GET','POST'])
def update_status(id,Status,LOCATION):

	NEW_CATTLE_STATUS = CATTLE_STATUS.update({'CATTLE_ID' : id}, {'CATTLE_ID' : id,'Status' : Status,'LOCATION' : LOCATION})
	return jsonify({'New Status of CATTLE_ID' : Status})
#   new_status_details = CATTLE_STATUS.find_one({'CATTLE_ID' : id})
#   output = {'Status' : new_status_details['Status']}

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
