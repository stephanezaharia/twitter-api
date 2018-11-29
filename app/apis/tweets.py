# app/apis/tweets.py
from flask_restplus import Namespace, Resource, fields
from flask import abort,request
from app.db import tweet_repository
from app.models import Tweet

api = Namespace('tweets')

model = api.model('Model', {
    'id': fields.Integer,
    'text': fields.String,
    "created_at": fields.DateTime
})

new=api.model('new tweet',{
    "text":fields.String(required=True,description="Tweet content")
    })

@api.route  ('/')
@api.response(404, 'Tweet not found')
class Tweetss(Resource):
    @api.expect(new,validate=True)
    @api.marshal_with(model,201)
    def post(self):
        tweet=Tweet(api.payload["text"])
        print(api.payload)
        tweet_repository.add(tweet)
        return tweet


@api.route('/<int:id>')
@api.doc(params={'id': 'An ID'})
@api.response(404, 'Tweet not found')
class Tweet(Resource):
    @api.marshal_with(model)
    def get(self, id):
        tweet = tweet_repository.get(id)

        if tweet is None:
            api.abort(404)
        else:
            return tweet

    def delete(self, id):
        tweet_repository.delete(id)
        return 201


