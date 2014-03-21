from app import db

class Article(db.Document):
	title = db.StringField()
	image_url = db.StringField()
	terms = db.ListField()

	def __unicode__(self):
		return self.title
