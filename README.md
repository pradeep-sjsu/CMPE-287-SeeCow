# CMPE-287-SeeCow
Reference Tutorial
https://github.com/pallets/flask/tree/1.0.2/examples/tutorial
http://flask.pocoo.org/docs/1.0/tutorial/#tutorial
Project Details
Source director under CMPE287.
/SeeCow

Install the required modules

python3 -m venv venv
pip install --upgrade
pip pip install -U Flask
python -m pip install pymongo[srv]
pip install flask_restful
pip install Flask-PyMongo
pip install -U flask-cors

Set up virtual python environment for SeeCow and initiate the API Server using flask

source venv/bin/activate
export FLASK_APP=warriors_rest_api.py
export FLASK_ENV=development
flask run --host=0.0.0.0

nohup flask run --host=0.0.0.0 &
