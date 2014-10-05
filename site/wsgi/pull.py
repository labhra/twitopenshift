"""
	Student Name: Laura Duggan, Student Number:07314299, Date: 30/7/14
	Class to pull tweets from twitter streaming API
"""

import sys
import codecs
sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')
from database import *
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
from alchemyapi import AlchemyAPI


class Pull(object):
	def __init__(self, query, maxTweet):
		#pass in auth details
		self.ckey = 'CVtJtQ4GNybpv0v9JVpQs7TS3'
		self.csecret = 'xE5uyc1fZjSfvdImaotwO79oiq2DWImeIZnVHtXcDCby0APqo4'
		self.atoken = '273450148-azU5GtOidHPiE9ejrPuvFE7fGztl4l58kVYg5jEh'
		self.asecret = 'QJf6FORBROH5s7Zr5pxBrJVMZYz1ceq6EMx4LDkphlFYx'
		#pass in query and max number of tweets
		self.query = query
		self.maxTweet = maxTweet

		#auth
		self.auth = OAuthHandler(self.ckey, self.csecret)
		self.auth.set_access_token(self.atoken, self.asecret)

		#set up listener with max tweets and query details
		self.twitterStream = Stream(self.auth, self.Listener(self.maxTweet))
		self.twitterStream.filter(track=[self.query]) 
		
		
	class Listener(StreamListener):
		def __init__(self, maxTweet, api=None):
			#set counter to 0
			self.tweetCounter = 0 
			#connect to database and create table
			self.database = Database()
			self.database.createTable()
			self.maxTweet = maxTweet

		#while data is arriving
		def on_data(self, data):
			try:
					
				#create alchemy api object
				alchemyapi = AlchemyAPI() 
				
				#check is json
				if (data.isdigit()):
					return True

				#load tweet data
				jsonData = json.loads(data)

				
				#make sure in english
				if jsonData['lang'] == "en":
					#find sentiment
					response = alchemyapi.sentiment("text", jsonData['text'])
					sentiment = response["docSentiment"]["type"]
					
					#find score, 'neutral' returns null to catch and set to 0
					try:
						scoreString = response["docSentiment"]["score"]
						score = float(scoreString)
						
					except:
						score = 0
					
					#add to dict
					dictionaryToDatabase = {"text" : jsonData['text'],
						 "lang" : jsonData['lang'], "screen_name" : jsonData['user']['screen_name'], "name" : jsonData['user']['name'], "image": jsonData['user']['profile_image_url'],"sentiment" : sentiment, "score" : score, "created_at" : jsonData['created_at'][:10] }
					
					
					#populate table
					self.database.popTable(dictionaryToDatabase)
					self.tweetCounter = self.tweetCounter + 1

				#if enough tweets grabbed stop counter
				if (self.tweetCounter >= self.maxTweet):
					result = self.database.showAll()
					return False
						
				else:
					return True
					
					
			except BaseException, e: #baseexception - any exception
				return True
				
				
		def on_error(self, status):
			return True
