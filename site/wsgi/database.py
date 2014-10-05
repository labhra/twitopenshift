"""
	Student Name: Laura Duggan, Student Number:07314299, Date: 30/7/14
	Database class creates tables and performs select statements on them.
"""

import pymysql
import sys

class Database:
	#connect to database and create cursor
	def __init__(self):
		self.db = pymysql.connect(host="mysql://$OPENSHIFT_MYSQL_DB_HOST:$OPENSHIFT_MYSQL_DB_PORT/", user="adminbgtsu6e", passwd="R7sKlbePFzfc", db="python	", charset="utf8")
		self.cur = self.db.cursor()

	#create 'tweet' talbe
	def createTable(self):
		self.cur.execute("DROP TABLE IF EXISTS tweet;")	
		self.cur.execute("CREATE TABLE tweet(text VARCHAR(180), lang VARCHAR(10), screen_name VARCHAR(20), name VARCHAR(20), image VARCHAR(150), sentiment VARCHAR(10), score FLOAT, created_at VARCHAR(40))")

	#populate 'tweet' table
	def popTable(self, dict):
		self.cur.execute("INSERT INTO tweet(text, lang, screen_name, name, image, sentiment, score, created_at) VALUES (%(text)s, %(lang)s, %(screen_name)s, %(name)s, %(image)s, %(sentiment)s, %(score)s, %(created_at)s)", dict)
		self.db.commit()

	#close connection to database
	def close(self):
		self.db.close()

	#return positive tweets
	def showPositive(self):
		self.positives = []
		self.cur.execute("SELECT * FROM tweet WHERE sentiment=\"positive\";")
		self.rows = self.cur.fetchall()
		self.count = self.cur.rowcount
		self.positives.append(self.count)
		self.positives.append(self.rows)
		return self.positives

	#return negative tweets
	def showNegative(self):
		self.negatives = []
		self.cur.execute("SELECT * FROM tweet WHERE sentiment=\"negative\";")
		self.rows = self.cur.fetchall()
		self.count = self.cur.rowcount
		self.negatives.append(self.count)
		self.negatives.append(self.rows)
		return self.negatives

	#return neutral tweets
	def showNeutral(self):
		self.neutrals = []
		self.cur.execute("SELECT * FROM tweet WHERE sentiment=\"neutral\";")
		self.rows = self.cur.fetchall()
		self.count = self.cur.rowcount
		self.neutrals.append(self.count)
		self.neutrals.append(self.rows)
		return self.neutrals

	#return all tweets
	def showAll(self):
		self.cur.execute("SELECT * FROM tweet;")
		self.rows = self.cur.fetchall()
		return self.rows

	#return breakdown of p/ne/nu tweets
 	def breakdown(self):
 		self.bd = []
 		self.positive = self.showPositive()[0]
 		self.negative = self.showNegative()[0]
 		self.neutral = self.showNeutral()[0]
 		self.bd.append(self.positive)
 		self.bd.append(self.negative)
 		self.bd.append(self.neutral)
 		return self.bd

 	#returns list of sentiment scores for each tweet
 	def scores(self):
 		self.cur.execute("SELECT score FROM tweet;")
 		self.scoresList=[self.element[0] for self.element in self.cur.fetchall()]
 		return self.scoresList

 	#creates 'graph' table
 	def createTableGraph(self):
		self.cur.execute("DROP TABLE IF EXISTS graph;")	
		self.cur.execute("CREATE TABLE graph(score FLOAT, created_at VARCHAR(40))")

	#populate graph table
	def popTableGraph(self, dict):
		self.cur.execute("INSERT INTO graph(score, created_at) VALUES (%(score)s, %(created_at)s)", dict)
		self.db.commit()

	#returns list of sentiment scores for each tweet in graph table
	def findScoreGraph(self):
		self.cur.execute("SELECT score, created_at FROM graph;")
		self.rows = self.cur.fetchall()
		return self.rows
