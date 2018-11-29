from unittest import TestCase
from app.models import Tweet
from app.repositories import TweetRepository  # We will code our `Tweet` class in `app/models.py`

class TestRepositories(TestCase):
    def test_repositories(self):
        r=TweetRepository()
        self.assertNotEqual(r,None)

    def test_add(self):
        r=TweetRepository()

        r.add(Tweet("Welcome"))
        self.assertEqual(len(r.data),1)

    def test_get_found(self):
        r=TweetRepository()
        r.add(Tweet("Welcome"))
        tweet=r.get(0)
        #print(tweet)
        self.assertEqual(tweet.text,"Welcome")
        self.assertEqual(tweet.id,0)

    def test_delet_found(self):
        r=TweetRepository()
        r.add(Tweet("Welcome"))
        r.delete(0)
        self.assertEqual(len(r.data),0)
