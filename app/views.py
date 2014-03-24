from flask import request, redirect, render_template, url_for, jsonify
from flask.views import MethodView
from app import app
from app.models import Article
import json, simplejson
import re
from urllib2 import Request, build_opener, HTTPError, URLError, urlopen
from bson import json_util
from flask.ext.mongoengine import MongoEngine


NUM_RESULTS = 5

GUARDIAN_ROOT = 'http://content.guardianapis.com/search?q='
GUARDIAN_FIELDS = 'show-fields=thumbnail'
GUARDIAN_PAGE_SIZE = 'page-size=' + str(NUM_RESULTS)


@app.route('/fetch_news')
def fetch_news():
	"""
	1) Parses the search term from the url
	2) Queries the Guardian API using the term
	3) Adds a selection of the results to API
	"""

	# 1)
	# Parse the search term from the url
	term = request.args.get('term')
	term = sp_to_plus(term)

	# 2)
	# Set up the query_url
	query_url = GUARDIAN_ROOT + term + '&' + GUARDIAN_FIELDS + '&' + GUARDIAN_PAGE_SIZE

	# Query the Guadian API
	try:
		the_request = Request(query_url)
	except HTTPError as e:
		print e.code
		print e.read
	except URLError as e:
		print 'We failed to reach a server.'
		print 'Reason: ', e.readon
	else:
		opener = build_opener()
		f = opener.open(the_request)
		json_obj = simplejson.load(f)

	# Parse the returned json_obj to get the first 5
	resp = json_obj["response"]
	results = resp["results"]

	# 3)
	# Loop through a number of the results objects
	for result in results:

		# Get the fields json object
		fields = result["fields"]

		# Create and save a new article document
		article = Article(title=result["webTitle"],
			image_url=fields["thumbnail"],
			terms=[term])
		article.save()

	return "Stored %d documents containing the search term: '%s'" % (len(results), term)


# Helper function: converts ' ' to '+' in search term
def sp_to_plus(term):
	return re.sub(r"\s+", '+', term)


class ArticleList(MethodView):
	"""
	Parses the search term(s) and returns a list of 
	relevant articles.
	"""

	def get(self):
		term = request.args.get('term')
		if term is None:
			return "You need to specify a search term...you fool."
		else:
			term = sp_to_plus(term)
			articles = Article.objects(terms__icontains=term)
			return articles.to_json()


class ArticleDetail(MethodView):

	def get(self, object_id):
		article = Article.objects(pk=object_id)
		return article.to_json()

	def post(self):
		article_json = request.json
		article_id = article_json["id"]
		article_title = article_json["title"]

		Article.objects(id=article_id).update_one(set__title=article_title)

		return "Article updated."

# Register the URLs
app.add_url_rule('/articles',
	view_func=ArticleList.as_view('article_list'))

article_view = ArticleDetail.as_view('article_detail')
app.add_url_rule('/article/<object_id>',
	view_func=article_view,
	methods=['GET',])
app.add_url_rule('/article',
	view_func=article_view,
	methods=['POST',])
