"""
	Student Name: Laura Duggan, Student Number:07314299, Date: 30/7/14
	Bottle script outlines routes for web app
"""

from bottle import route, run, template, request, static_file, view, SimpleTemplate, Bottle, url
from database import *
from pull import *
import sys
import codecs
sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')
import os
from searchpuller import *
from datetime import datetime, timedelta

#create and return homepage
@route('/home', method=['GET', 'POST']) 
def home():
		output = template('views/homePage')
		return output

#create results page for search API
@route('/resultsSearch', method=['GET', 'POST'])
def resultsSearch():
	if request.POST.get('searchFind', '').strip():
		
		#open database connection and create 'tweet' table for results
		db = Database()
		db.createTable()

		#find how many tweets are required from user
		maxTweetString = request.POST.get('searchMaxnum', '').strip()
		maxTweet = int(maxTweetString)

		#find the query from user
		query = request.POST.get('searchSearch', '').strip()

		#find results type desired
		resultType = request.POST.get('resulttype', '').strip()

		#find how many days of results are required
		daysString = request.POST.get('days', '').strip()
		days = int(daysString)

		
		minusDays = 1
		nowDate = datetime.now().strftime("20%y-%m-%d")
		while (days > 0):
			#create puller for tweets for however many days required
			puller = Searchpuller(query, maxTweet, resultType, nowDate, "tweet") #for is table tweet
			days = days - 1
			nowDate = (datetime.now() - timedelta(days=minusDays)).strftime("20%y-%m-%d")
			minusDays = minusDays + 1

		#feed results into results list
		results = db.showAll()

		#feed breakdown p/ne/nu into breakdown list
		breakdown = db.breakdown()

		#feed scores into scores list
		scores = db.scores()

		#show output
		output = template('views/resultsPage', query=query, results=results, breakdown=breakdown, tweets=maxTweet, scores=scores, resultType=resultType)
		return output


#create results page from stream API
@route('/resultsStream', method=['GET', 'POST']) #create results page
def resultsStream():
  if request.POST.get('streamFind', '').strip():
    
    #find now many tweets required
    maxTweetString = request.POST.get('streamMaxnum', '').strip()
    maxTweet = int(maxTweetString)
    
   	#find query
    query = request.POST.get('streamSearch', '').strip()
    
    #connect to database
    db = Database()

    #pull tweets
    puller = Pull(query, maxTweet)

    #feed showall into results
    results = db.showAll()

    #feed breakdown p/ne/nu into breakdown
    breakdown = db.breakdown()

    #feed scores into scores list
    scores = db.scores()

    #show output
    output = template('views/resultsPage', query=query, results=results, breakdown=breakdown, tweets=maxTweet, scores=scores)
    return output

#create update route for updating timeline, to be called by cron
@route('/update', method=['GET', 'POST'])
def update():
	#connect to database
	db = Database()

	#set nowDate to today & format
	nowDate = (datetime.now() - timedelta(days=1)).strftime("20%y-%m-%d")

	#pull 100 tweets for desired query
	puller = Searchpuller("dublin", 100, "recent", nowDate, "graph") #for is table graph
	
#create timeline page
@route('/timeline', method=['GET', 'POST'])
def timeline():
	#connect to database
	db = Database()

	#connect all results into list of tuples
	results = db.findScoreGraph()

	#show output
	output = template('views/timelinePage', results=results, query="Dublin")
	return output

#create about page
@route('/about', method=['GET', 'POST'])
def about():
	#show output
	output = template('views/aboutPage')
	return output

#create contact page
@route('/contact', method=['GET', 'POST'])
def contact():
	#show output
	output = template('views/contactPage')
	return output

#handlers for static files
@route('/static/css/<filename>')
def server_static(filename):
	return static_file(filename, root='\static\css\\')   

@route('/static/js/<filename>')
def server_static(filename):
	return static_file(filename, root='\static\js\\')

@route('/static/fonts/<filename>')
def server_static(filename):
	return static_file(filename, root='\static\fonts\\')

@route('/static/img/<filename>')
def server_static(filename):
	return static_file(filename, root='\static\img\\')




