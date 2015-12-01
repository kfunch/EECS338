import sys
import urllib
import urllib2
import json
from bs4 import BeautifulSoup
from bagOfWordsUrlTopTwo import bagOfWordsUrlTopTwo
from bagOfWordsByParagraph import bagOfWordsByParagraph
from findSentence import findSentence
from bagOfWordsGivenParagraphs import bagOfWordsGivenParagraphs
from bing_api import bing_api
import re

def googleSearch(searchTerm):
#
#   AUTHOR: Kristin Funch
	print searchTerm
	print '\n\n'
	topRelatedWords = []
	relevantWords = ' '
	result1 = ''
	result2 = ''
	result3 = ''
	result4 = ''
	top2 = []

	print 'ANECDOTE\n'
	#ANECDOTE
	query = "\"when I first heard about " + searchTerm + "\""	#exact phrasing
	results4 = bing_api(query)
	if (len(results4['d']['results']) < 1):	#if no results from exact phrasing
		query = "when I first heard about " + searchTerm 	#inexact phrasing
		results4 = bing_api(query)
	elif (len(results4['d']['results']) < 5):	#if < 5 results from exact phrasing
		query = "when I first heard about " + searchTerm 	#inexact phrasing
		results4['d']['results'] = [x for x in (bing_api(query)['d']['results'] + results4['d']['results'])]	#combine results

	paragraphArr = []
	cleanParagraphArr = []
	searchTermParArr = []
	cleanSearchTermParArr = []
	indices = []
	searchTermIndices = []
	for x in range(0, len(results4['d']['results'])):
		url = results4['d']['results'][x]['Url']
		paragraphs = findSentence(url, searchTerm, 'when I first heard about ', '', 1) #search for exact phrase
		if (len(paragraphs[0]) < 1):
			paragraphs = findSentence(url, searchTerm, 'when I first heard about ', '', 0) #search for paragraph containing fragments
		for y in range(0, len(paragraphs[0])):	#if paragraphs found
			if (paragraphs[2]):	#if exact phrasing found
				paragraphArr.append(paragraphs[0][y])
				cleanParagraphArr.append(paragraphs[1][y])
				indices.append(x)
			else:	#if partial
				searchTermParArr.append(paragraphs[0][y])
				cleanSearchTermParArr.append(paragraphs[1][y])
				searchTermIndices.append(x)
	if (len(paragraphArr) < 1):	#if exact phrasing not found
		paragraphArr = searchTermParArr
		cleanParagraphArr = cleanSearchTermParArr
		indices = searchTermIndices
	if (len(cleanParagraphArr) > 0):	#if any paragraphs found
		parIndex = bagOfWordsGivenParagraphs(cleanParagraphArr, top2)[1]	#best ranked by anecdote keywords
		top2 = bagOfWordsUrlTopTwo(results4['d']['results'][indices[parIndex]]['Url'], searchTerm)	#top two words on page not in search term
		relevantWords = relevantWords + top2[0] + ' ' + top2[1] + ' '
		print top2[0]
		print '\n'
		print top2[1]
		print '\n'
		result1 = paragraphArr[parIndex]
		print result1
		print '\n'

	print 'PROBLEM\n'
	#PROBLEM
	query = "\"the problem with " + searchTerm + " is\""	#exact phrasing
	results4 = bing_api(query)
	if (len(results4['d']['results']) < 1):	#if no results from exact phrasing
		query = "the problem with " + searchTerm + relevantWords	#inexact with top relevant words
		results4 = bing_api(query)
	elif (len(results4['d']['results']) < 5):	#elif < 5 results from exact phrasing
		query = "the problem with " + searchTerm + relevantWords	#inexact with top relevant words
		results4['d']['results'] = [x for x in (bing_api(query)['d']['results'] + results4['d']['results'])]	#combine results
	
	if (len(results4['d']['results']) < 1): #if still no results
		query = "the problem with " + searchTermIndices	#search without top relevant words
		results4 = bing_api(query)
		print len(results4['d']['results'])
	elif (len(results4['d']['results']) < 5):	#elif still < 5 results
		query = "the problem with " + searchTermIndices	#search without top relevant words
		results4['d']['results'] = [x for x in (bing_api(query)['d']['results'] + results4['d']['results'])]	#combine results

	paragraphArr = []
	cleanParagraphArr = []
	for x in results4['d']['results']:
		url = x['Url']
		paragraphs = findSentence(url, searchTerm, 'the problem with ', ' is', 1)	#search for exact phrase
		if (len(paragraphs[0]) < 1):	#if exact phrase not found
			paragraphs = findSentence(url, searchTerm, 'the problem with ', ' is', 0)	#search for paragraphs containing fragments
		for y in range(0, len(paragraphs[0])):
			paragraphArr.append(paragraphs[0][y])
			cleanParagraphArr.append(paragraphs[1][y])
	if (len(cleanParagraphArr) > 0):
		result2 = paragraphArr[bagOfWordsGivenParagraphs(cleanParagraphArr, top2)[0]]
		print result2
		print '\n'

	print 'WIKIPEDIA\n'
	#WIKI
	query = searchTerm + relevantWords + ' site:en.wikipedia.org'
	results = bing_api(query)
	if (len(results['d']['results']) < 1):	#if no results
		query = searchTerm + ' site:en.wikipedia.org'	#search without top relevant words
		results = bing_api(query)

	if (len(results['d']['results']) > 0):
		for x in range(0, 1):
			url = results['d']['results'][x]['Url']
			result3 = re.sub(r'\[[^\]]*\]', ' ', bagOfWordsByParagraph(url)[0])	#remove anything between square brackets
			result3 = re.sub(r'\<[^\>]*\>', ' ', result3)	#remove anything between angle brackets
			result3 = re.sub(r'\([^\)]*\)', ' ', result3)	#remove anything between parentheses
			print result3
			print '\n'

	print 'SOLUTION\n'
	#SOLUTION
	query = "\"solution to " + searchTerm + "\""	#exact phrasing
	results4 = bing_api(query)
	if (len(results4['d']['results']) < 1):	#if no results from exact phrasing
		query = "solution to " + searchTerm + relevantWords	#search with top relevant words
		results4 = bing_api(query)
	elif (len(results4['d']['results']) < 5):	#if < 5 results from exact phrasing
		query = "solution to " + searchTerm + relevantWords	#search with top relevant words
		results4['d']['results'] = [x for x in (bing_api(query)['d']['results'] + results4['d']['results'])]	#combine results

	if (len(results4['d']['results']) < 1):	#if still no results
		query = "solution to " + searchTerm 	#search without top relevant words
		results4 = bing_api(query)
	elif (len(results4['d']['results']) < 5):	#if still < 5 results
		query = "solution to " + searchTerm 	#search without top relevant words
		results4['d']['results'] = [x for x in (bing_api(query)['d']['results'] + results4['d']['results'])]	#combine results

	paragraphArr = []
	cleanParagraphArr = []
	searchTermParArr = []
	cleanSearchTermParArr = []
	for x in results4['d']['results']:
		url = x['Url']
		paragraphs = findSentence(url, searchTerm, 'solution to ', '', 1)
		if (len(paragraphs[0]) < 1):
			paragraphs = findSentence(url, searchTerm, 'solution to ', '', 0)
		for y in range(0, len(paragraphs[0])):
			if (paragraphs[2]):
				paragraphArr.append(paragraphs[0][y])
				cleanParagraphArr.append(paragraphs[1][y])
			else:
				searchTermParArr.append(paragraphs[0][y])
				cleanSearchTermParArr.append(paragraphs[1][y])
	if (len(paragraphArr) < 1):
		paragraphArr = searchTermParArr
		cleanParagraphArr = cleanSearchTermParArr
	if (len(cleanParagraphArr) > 0):
		parIndex = bagOfWordsGivenParagraphs(cleanParagraphArr, top2)[2]
		print paragraphArr[parIndex]
		result4 = paragraphArr[parIndex]
		print '\n'

	return [result1, result2, result3, result4]


def main():
	# read in system arguments
	searchTerm = sys.argv[1]
	googleSearch(searchTerm)

if __name__ == "__main__":
	main()