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

	print 'ANECDOTE\n'
	#ANECDOTE
	query = "\"when I first heard about " + searchTerm + "\""
	results4 = bing_api(query)
	#print len(results4['d']['results'])
	if (len(results4['d']['results']) < 1):
		query = "when I first heard about " + searchTerm
		results4 = bing_api(query)
	elif (len(results4['d']['results']) < 5):
		query = "when I first heard about " + searchTerm
		#c = {key: value for (key, value) in (a.items() + b.items())}
		results4['d']['results'] = [x for x in (bing_api(query)['d']['results'] + results4['d']['results'])]
	#print len(results4['d']['results'])
	paragraphArr = []
	cleanParagraphArr = []
	searchTermParArr = []
	cleanSearchTermParArr = []
	indices = []
	searchTermIndices = []
	for x in range(0, len(results4['d']['results'])):
		url = results4['d']['results'][x]['Url']
		paragraphs = findSentence(url, searchTerm, 'when I first heard about ', '', 1)
		if (len(paragraphs[0]) < 1):
			paragraphs = findSentence(url, searchTerm, 'when I first heard about ', '', 0)
		for y in range(0, len(paragraphs[0])):
			if (paragraphs[2]):
				paragraphArr.append(paragraphs[0][y])
				cleanParagraphArr.append(paragraphs[1][y])
				indices.append(x)
			else:
				searchTermParArr.append(paragraphs[0][y])
				cleanSearchTermParArr.append(paragraphs[1][y])
				searchTermIndices.append(x)
	if (len(paragraphArr) < 1):
		paragraphArr = searchTermParArr
		cleanParagraphArr = cleanSearchTermParArr
		indices = searchTermIndices
	if (len(cleanParagraphArr) > 0):
		parIndex = bagOfWordsGivenParagraphs(cleanParagraphArr)[1]
		top2 = bagOfWordsUrlTopTwo(results4['d']['results'][indices[parIndex]]['Url'], searchTerm)
		#top2 = bagOfWordsUrlTopTwo(results4[indices[parIndex]]['url'], searchTerm)
		relevantWords = relevantWords + top2[0] + ' ' + top2[1] + ' '
		print top2[0]
		print '\n'
		print top2[1]
		print '\n'
		print paragraphArr[parIndex]
		result1 = paragraphArr[parIndex]
		print '\n'

	print 'PROBLEM\n'
	#PROBLEM
	query = "\"the problem with " + searchTerm + " is\""
	results4 = bing_api(query)
	if (len(results4['d']['results']) < 1):
		query = "the problem with " + searchTerm + relevantWords
		results4 = bing_api(query)

	paragraphArr = []
	cleanParagraphArr = []
	for x in results4['d']['results']:
		url = x['Url']
		paragraphs = findSentence(url, searchTerm, 'the problem with ', ' is', 1)
		if (len(paragraphs[0]) < 1):
			paragraphs = findSentence(url, searchTerm, 'the problem with ', ' is', 0)
		for y in range(0, len(paragraphs[0])):
			paragraphArr.append(paragraphs[0][y])
			cleanParagraphArr.append(paragraphs[1][y])
	if (len(cleanParagraphArr) > 0):
		print paragraphArr[bagOfWordsGivenParagraphs(cleanParagraphArr)[0]]
		result2 = paragraphArr[bagOfWordsGivenParagraphs(cleanParagraphArr)[0]]
		print '\n'

	print 'WIKIPEDIA\n'
	#WIKI
	#query = searchTerm + relevantWords + ' site:en.wikipedia.org'
	query = searchTerm + relevantWords + ' site:en.wikipedia.org'
	results = bing_api(query)

	for x in range(0, 1):
		url = results['d']['results'][x]['Url']
		print bagOfWordsByParagraph(url)[0]
		result3 = bagOfWordsByParagraph(url)[0]
		print '\n'

	print 'SOLUTION\n'
	#SOLUTION
	#query = "\"solution to " + searchTerm + "\"" + relevantWords
	query = "\"solution to " + searchTerm + "\""
	results4 = bing_api(query)
	if (len(results4['d']['results']) < 1):
		query = "solution to " + searchTerm + relevantWords
		results4 = bing_api(query)

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
		parIndex = bagOfWordsGivenParagraphs(cleanParagraphArr)[2]
		print paragraphArr[parIndex]
		result4 = paragraphArr[parIndex]
		print '\n'

	return [result1, result2, result3, result4]


def main():
	# read in system arguments
	searchTerm = sys.argv[1]
	#google_search(searchTerm)
	googleSearch(searchTerm)

if __name__ == "__main__":
	main()