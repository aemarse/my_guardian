import json
import unittest
import urllib2

import app
from app.models import Article

class AppTestCase(unittest.TestCase):


	def setUp(self):
		self.app = app.app.test_client()
		self.search = '?term='
		self.search_term = 'john+kerry'


	def tearDown(self):
		pass


	def test_article_created(self):
		response = self.app.get('/fetch_news' + self.search + self.search_term)

		self.assertEquals('200 OK', response.status)


	def test_get_articles_from_term(self):
		response = self.app.get('/articles' + self.search + self.search_term)
		articles = Article.objects(terms__icontains=self.search_term)

		self.assertIsNotNone(articles)
		self.assertEquals('200 OK', response.status)


	def test_get_article_from_object_id(self):

		# Test data
		test_title = 'Test 1'
		test_image_url = '/Test 1'
		test_terms = ['Test']

		# Create a dummy article for testing
		test_article = Article(
			title=test_title,
			image_url=test_image_url,
			terms=test_terms,
		)
		test_article.save()

		# Get the ObjectId of the dummy article
		object_id = test_article.id

		# Query the db for the article
		response = self.app.get('/article/' + str(object_id))
		json_string = response.get_data()

		# Get dict from json string
		json_list = json.loads(json_string)
		json_dict = json_list[0]

		# Get data from dict
		title = json_dict['title']
		image_url = json_dict['image_url']
		terms = json_dict['terms']

		# Check returned data against original data
		self.assertEquals(title, test_title)
		self.assertEquals(image_url, test_image_url)
		self.assertEquals(terms, test_terms)

		# Check our response status also
		self.assertEquals('200 OK', response.status)


	def test_post_article_from_object_id(self):

		# Test data
		test_title = 'Test 1'
		test_image_url = '/Test 1'
		test_terms = ['Test']

		# Create a dummy article for testing
		test_article = Article(
			title=test_title,
			image_url=test_image_url,
			terms=test_terms,
		)
		test_article.save()

		# Get the ObjectId of the dummy article
		object_id = test_article.id

		# Set the new title
		new_title = 'New Title'

		url = 'http://127.0.0.1:5000/article '
		data = '{"id":"' + str(object_id) + '", "title": "' + new_title + '"}'

		req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
		response = urllib2.urlopen(req)
		json_string = response.read()

		# Get dict from json string
		json_list = json.loads(json_string)
		json_dict = json_list

		# Get data from dict
		title = json_dict['title']

		# Check returned data against original data
		self.assertEquals(title, new_title)

		# Check our response status also
		self.assertEquals(200, response.getcode())


if __name__ == '__main__':
	unittest.main()
