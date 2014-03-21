from flask import Flask
from flask.ext.mongoengine import MongoEngine


db_name = "my_guardian"
mongo_uri = "mongodb://aemarse:elpenguino@oceanic.mongohq.com:10041/my_guardian"

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': db_name, "host": mongo_uri}
app.config["SECRET_KEY"] = "shhh"

db = MongoEngine(app)

if __name__ == '__main__':
	app.run()
