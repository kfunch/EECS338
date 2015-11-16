import sys
import urllib
import urllib2
import json
from bs4 import BeautifulSoup
from bagOfWords import bagOfWords
from bagOfWordsByParagraph import bagOfWordsByParagraph
from findSentence import findSentence
from bagOfWordsGivenParagraphs import bagOfWordsGivenParagraphs

def googleSearch():
#
#   AUTHOR: Kristin Funch
	print '\n\n'
	searchTerm = raw_input('Query: ')
	print '\n\n'
	topRelatedWords = []

	#PROBLEM
	query = "\"when I first heard about\" " + searchTerm
	query = urllib.urlencode ( { 'q' : query } )
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	json1 = json.loads ( response )
	results4 = json1 [ 'responseData' ] [ 'results' ]

	paragraphArr = []
	cleanParagraphArr = []
	for x in range(0, len(results4)):
		url = results4[x]['url']
		paragraphs = findSentence(url, '', 'when I first heard about', '')
		for x in range(0, len(paragraphs[0])):
			paragraphArr.append(paragraphs[0][x])
			cleanParagraphArr.append(paragraphs[1][x])
	print paragraphArr[bagOfWordsGivenParagraphs(cleanParagraphArr)[1]]
	print '\n'

	#PROBLEM
	query = "\"the problem with " + searchTerm + " is\""
	query = urllib.urlencode ( { 'q' : query } )
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	json1 = json.loads ( response )
	results4 = json1 [ 'responseData' ] [ 'results' ]

	paragraphArr = []
	cleanParagraphArr = []
	for x in range(0, len(results4)):
		url = results4[x]['url']
		paragraphs = findSentence(url, searchTerm, 'the problem with ', ' is')
		for x in range(0, len(paragraphs[0])):
			paragraphArr.append(paragraphs[0][x])
			cleanParagraphArr.append(paragraphs[1][x])
	print paragraphArr[bagOfWordsGivenParagraphs(cleanParagraphArr)[0]]
	print '\n'

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
		print '\n'

	#SOLUTION
	query = "\"solution to " + searchTerm + "\""
	query = urllib.urlencode ( { 'q' : query } )
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	json1 = json.loads ( response )
	results4 = json1 [ 'responseData' ] [ 'results' ]

	paragraphArr = []
	cleanParagraphArr = []
	for x in range(0, len(results4)):
		url = results4[x]['url']
		paragraphs = findSentence(url, searchTerm, 'solution to ', '')
		for x in range(0, len(paragraphs[0])):
			paragraphArr.append(paragraphs[0][x])
			cleanParagraphArr.append(paragraphs[1][x])
	print paragraphArr[bagOfWordsGivenParagraphs(cleanParagraphArr)[2]]
	print '\n'

def main():
	# read in system arguments
	#searchTerm = sys.argv[1]
	#google_search(searchTerm)
	googleSearch()

if __name__ == "__main__":
	main()