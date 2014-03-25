Hello Ethan and Sundar. Thanks again for giving me the opportunity to show you my skills through this code test. I look forward to going through it with you. Let me know if you have any questions/problems running any of this.

BTW, I'm using MongoHQ to host my database, and I already gave you an account (username:ethan, password:ethan). You shouldn't need this info though, since the db connection happens automatically in app/__init__.py

TESTING OUT THE URLS:
- GET /fetch_news
	- Ex: http://my-guardian-code.herokuapp.com/fetch_news?term=john+kerry

- GET /articles
	- Ex: http://my-guardian-code.herokuapp.com/articles?term=john+kerry

- GET /article/<ObjectId>
	- Ex: http://my-guardian-code.herokuapp.com/article/5330a943e311e400075e8d82

- POST /article
	- I've been running this from Terminal using curl
	- Ex: curl -H "Content-type: application/json" -X POST http://my-guardian-code.herokuapp.com/article -d '{"id":"5330a943e311e400075e8d82", "title": "New Title"}'

RUNNING THE TEST CASES
- from the main directory of the app, run:
	python -m tests.test
- by the way, the test.py app uses localhost:5000 to perform the last test, so you'll have to run the code locally...sorry about that.

TO DROP THE ARTICLE COLLECTION FROM THE DB
- from the main directory of the app, run:
	python -m tests.drop_coll

