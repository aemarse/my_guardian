from app import db
from flask import jsonify

class Article(db.Document):
	title = db.StringField()
	image_url = db.StringField()
	terms = db.ListField()

	def __unicode__(self):
		return self.title
