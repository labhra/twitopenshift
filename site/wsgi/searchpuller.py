"""
	Student Name: Laura Duggan, Student Number:07314299, Date: 30/7/14
	Class to pull tweets from twitter search API
"""


import sys
import codecs
sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')
from database import *
import twitter
from alchemyapi import AlchemyAPI

class Searchpuller(object):
	def __init__(self, query, maxTweet, resultType, nowDate, tweetOrGraph):
		#authenticate and create instance of twitter search API
		self.api = twitter.Api(
			consumer_key = 'CVtJtQ4GNybpv0v9JVpQs7TS3',
			consumer_secret = 'xE5uyc1fZjSfvdImaotwO79oiq2DWImeIZnVHtXcDCby0APqo4',
			access_token_key = '273450148-azU5GtOidHPiE9ejrPuvFE7fGztl4l58kVYg5jEh',
			access_token_secret = 'QJf6FORBROH5s7Zr5pxBrJVMZYz1ceq6EMx4LDkphlFYx'
			)

		#connect to database
		self.database = Database()

		#pass through arguements
		self.query = query
		self.maxTweet = maxTweet
		self.resultType = resultType
		self.nowDate = nowDate
		self.tweetOrGraph = tweetOrGraph

		#search for tweets and save to self.search
		self.search = self.api.GetSearch(term=self.query, lang='en', result_type=resultType, count=self.maxTweet, max_id='', until=self.nowDate)

		#for each tweet
		for t in self.search:
			#create AlchempyAPI object
			alchemyapi = AlchemyAPI()

			#find sentiment type
			response = alchemyapi.sentiment("text", t.text)
			sentiment = response["docSentiment"]["type"]

			#find sentiment score, 'neutal' returns none, so catch and assign 0
			try:
				scoreString = response["docSentiment"]["score"]
				score = float(scoreString)
			except:
				score = 0

			#if it's for the tweet table 
			if (tweetOrGraph == "tweet"):
				dictionaryToDatabase = {"text" : t.text, "lang" : t.lang, "screen_name" : t.user.screen_name, "name" : t.user.name, "image" :t.user.profile_image_url, "sentiment" : sentiment, "score" : score, "created_at" : t.created_at[:10]}

				#populate tweet table
				self.database.popTable(dictionaryToDatabase)

			#if it's for the graph table
			else:
				dictionaryToDatabase = {"score" : score, "created_at" : t.created_at[3:10]}

				#populate graph table
				self.database.popTableGraph(dictionaryToDatabase)

