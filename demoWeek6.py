import sys
import urllib
import urllib2
import json
from bs4 import BeautifulSoup
from bagOfWords import bagOfWords

def googleSearch():
#
#   AUTHOR: Kristin Funch
	
	searchTerm = raw_input('Query: ')


	#DEBATE
	debateQuery = searchTerm + ' site:www.debate.org/opinions'
	query = urllib.urlencode ( { 'q' : debateQuery } )
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	json1 = json.loads ( response )
	results3 = json1 [ 'responseData' ] [ 'results' ]

	for x in range(0, 1):
		url = results3[x]['url']
		top2 = bagOfWords(url, 0, searchTerm)[3]
		print top2
		printDebate(url)

	#WIKI
	query = searchTerm + ' site:en.wikipedia.org'
	query = urllib.urlencode ( { 'q' : query } )
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	json1 = json.loads ( response )
	results = json1 [ 'responseData' ] [ 'results' ]

	for x in range(0, 1):
		url = results[x]['url']
		top2 = bagOfWords(url, 0, searchTerm)[3]
		print top2
		printWikipedia(url)

	#REDDIT
	redditQuery = searchTerm + ' site:www.reddit.com/r/self'
	query = urllib.urlencode ( { 'q' : redditQuery } )
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	json1 = json.loads ( response )
	results2 = json1 [ 'responseData' ] [ 'results' ]
	#for x in range(0, len(results2)):

	personalStoryRatings = []
	for x in range(0, len(results2)):
		url = results2[x]['url']
		bagOfWordsResults = bagOfWords(url, 1, searchTerm)
		personalStoryRatings.append(bagOfWordsResults[1])
		top2 = bagOfWordsResults[3]
		print top2
		
	print personalStoryRatings
	printReddit(results2[personalStoryRatings.index(max(personalStoryRatings))]['url'])

def printWikipedia(url):
		#print (url) + '\n'
		resp = urllib2.urlopen(url)
		html = resp.read()
		parsed_html = BeautifulSoup(html, 'lxml')

		if (parsed_html.body.find('div', attrs={'class':'mw-content-ltr'}) is None):
			#print (parsed_html.prettify()) + '\n'
			print 'error'
		else:
			print parsed_html.body.find('div', attrs={'class':'mw-content-ltr'}).find('p').text + '\n'

def printDebate(url):
		#print (url) + '\n'
		resp = urllib2.urlopen(url)
		html = resp.read()
		parsed_html = BeautifulSoup(html, 'lxml')

		if (parsed_html.body.find('span', attrs={'class':'q-title'}) is None):
			print 'error1'
		else:
			print parsed_html.body.find('span', attrs={'class':'q-title'}).text + '\n'

		if (parsed_html.body.find('div', attrs={'id':'yes-arguments'}).find('h2') is None):
			print 'error2'
		else:
			 print parsed_html.body.find('div', attrs={'id':'yes-arguments'}).find('h2').text + '\n'

		if (parsed_html.body.find('div', attrs={'id':'yes-arguments'}).find('p') is None):
			print 'error3'
		else:
			 print parsed_html.body.find('div', attrs={'id':'yes-arguments'}).find('p').text + '\n'

def printReddit(url):
		print (url) + '\n'
		hdr = { 'User-Agent' : 'NLP project test' }
		req = urllib2.Request(url, headers=hdr)
		resp = urllib2.urlopen(req)
		#resp = urllib2.urlopen(url)
		html = resp.read()
		parsed_html = BeautifulSoup(html, 'lxml')
		#print (parsed_html.prettify())
		#print parsed_html.body.find_all('p', limit=1)
		if (parsed_html.body.find('div', attrs={'class':'entry'}).find('div', attrs={'class':'usertext-body'}).find('p') is None):
			#print (parsed_html.prettify()) + '\n'
			print 'error'
		else:
			#print parsed_html.body.find('div', attrs={'class':'mw-content-ltr'}).text
			print parsed_html.body.find('div', attrs={'class':'entry'}).find('div', attrs={'class':'usertext-body'}).find('p').text + '\n'
	

def main():
	# read in system arguments
	#searchTerm = sys.argv[1]
	#google_search(searchTerm)
	googleSearch()

if __name__ == "__main__":
	main()