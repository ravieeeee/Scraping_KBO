from flask import Flask
from flask import request
from flask_pymongo import PyMongo
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
from bson.json_util import dumps

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ['kbo_mlab_uri']
mongo = PyMongo(app)
env = Environment(
	loader=FileSystemLoader('templates'),
	autoescape=select_autoescape('html')
)

def teamname_case_insensitive(team):
	if team == 'KT':
		return 'kt'
	elif team != 'kt':
		return team.upper()
	else:
		return team

@app.route('/')
def index_page():
	return env.get_template('index.html').render()

@app.route('/search')
def search_page():
	date = request.args.get('date')
	team = teamname_case_insensitive(request.args.get('team'))
	bson_result = mongo.db.erm.find({'date': date, 'team': team}, {'_id': False})
	result = dumps(bson_result, ensure_ascii=False)
	return env.get_template('search.html').render(result=result)

if __name__ == '__main__':
	app.run()
