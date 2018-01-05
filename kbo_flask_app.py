from flask import Flask
from flask_pymongo import PyMongo
from jinja2 import Environment, FileSystemLoader
import os
import bson
from bson.json_util import dumps

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ['kbo_mlab_uri']
mongo = PyMongo(app)
env = Environment(loader=FileSystemLoader('templates'))

@app.route('/')
def index_page():
	return env.get_template('index.html').render()

@app.route('/search/<date>')
def search_page(date):
	bson_result = mongo.db.erm.find_one_or_404({'date': date})
	result = dumps(bson_result, ensure_ascii=False)
	return env.get_template('result.html').render(result=result)
