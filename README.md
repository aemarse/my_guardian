Hello Ethan and Sundar. Thanks again for giving me the opportunity to show you my skills through this code test. I look forward to going through it with you. Let me know if you have any questions/problems running any of this.

BTW, I'm using MongoHQ to host my database, and I already gave you an account (username:ethan, password:ethan). You shouldn't need this info though, since the db connection happens automatically in app/__init__.py

TESTING OUT THE URLS:
- GET /fetch_news
	- Ex: localhost:5000/fetch_news?term=john+kerry

- GET /articles
	- Ex: localhost:5000/articles?term=john+kerry

- GET /article/<ObjectId>
	- Ex: localhost:5000/articles/533077f05946bae69363c547

- POST /article
	- I've been running this from Terminal using curl
	- Ex: curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/article -d '{"id":"533077f05946bae69363c547", "title": "New Title"}'

RUNNING THE TEST CASES
- from the main directory of the app, run:
	python -m tests.test

TO DROP THE ARTICLE COLLECTION FROM THE DB
- from the main directory of the app, run:
	python -m tests.drop_coll
