import sys
import urllib
import urllib2
import json
from bs4 import BeautifulSoup
from bagOfWords import bagOfWords
from bagOfWordsByParagraph import bagOfWordsByParagraph

def googleSearch():
#
#   AUTHOR: Kristin Funch
	print '\n\n'
	searchTerm = raw_input('Query: ')
	print '\n\n'
	topRelatedWords = []

	#DEBATE
	debateQuery = searchTerm + ' site:www.debate.org/opinions'
	query = urllib.urlencode ( { 'q' : debateQuery } )
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	json1 = json.loads ( response )
	results3 = json1 [ 'responseData' ] [ 'results' ]

	for x in range(0, 1):
		url = results3[x]['url']
		top2 = bagOfWords(url, 0, searchTerm)[3]
		topRelatedWords.append(top2[0])
		topRelatedWords.append(top2[1])
		print bagOfWordsByParagraph(url)[0]
		print '\n\n'

	#WIKI
	query = searchTerm + ' site:en.wikipedia.org'
	query = urllib.urlencode ( { 'q' : query } )
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	json1 = json.loads ( response )
	results = json1 [ 'responseData' ] [ 'results' ]

	for x in range(0, 1):
		url = results[x]['url']
		top2 = bagOfWords(url, 0, searchTerm)[3]
		topRelatedWords.append(top2[0])
		topRelatedWords.append(top2[1])
		print bagOfWordsByParagraph(url)[0]
		print '\n\n'

	#REDDIT
	redditQuery = searchTerm + ' site:www.reddit.com/r/self'
	query = urllib.urlencode ( { 'q' : redditQuery } )
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	json1 = json.loads ( response )
	results2 = json1 [ 'responseData' ] [ 'results' ]

	personalStoryRatings = []
	for x in range(0, len(results2)):
		url = results2[x]['url']
		bagOfWordsResults = bagOfWords(url, 1, searchTerm)
		personalStoryRatings.append(bagOfWordsResults[1])
		top2 = bagOfWordsResults[3]
		topRelatedWords.append(top2[0])
		topRelatedWords.append(top2[1])
		
	#print personalStoryRatings
	print bagOfWordsByParagraph(results2[personalStoryRatings.index(max(personalStoryRatings))]['url'])[1]
	print '\n\n'
	
	waPoQuery = searchTerm + ' solution site:www.washingtonpost.com/opinions/'
	query = urllib.urlencode ( { 'q' : waPoQuery } )
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	json1 = json.loads ( response )
	results4 = json1 [ 'responseData' ] [ 'results' ]

	solutionRatings = []
	for x in range(0, len(results4)):
		url = results4[x]['url']
		bagOfWordsResults = bagOfWords(url, 0, searchTerm)
		solutionRatings.append(bagOfWordsResults[2])
		top2 = bagOfWordsResults[3]
		topRelatedWords.append(top2[0])
		topRelatedWords.append(top2[1])

	if (solutionRatings != []):
		print bagOfWordsByParagraph(results4[solutionRatings.index(max(solutionRatings))]['url'])[2]
	print topRelatedWords

def main():
	# read in system arguments
	#searchTerm = sys.argv[1]
	#google_search(searchTerm)
	googleSearch()

if __name__ == "__main__":
	main()