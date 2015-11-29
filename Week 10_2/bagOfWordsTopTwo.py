import sys
import urllib
import urllib2
import json
import nltk
#from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup

def bagOfWordsTopTwo(visible_text, searchTerm):

	parsed_text = nltk.word_tokenize(visible_text)
	#print parsed_text

	#s=set(stopwords.words('english'))
	s = ['the', 'of', 'a', 'an', 'and', 'to', 'that', 'in', 'is', 'as', 'for', 'it', 'with', 'on', 'was', 'be', 'at',
		 'by', 'on', 'out', 'has', 'have', 'he', 'she', 'him', 'her', 'they', 'are', 'not', 'all', 'what',
		 'would', 'but', 'or', 'their', 'from', 'like', 'had', 'about', 'which', 'were', 'just', 'if', 'when', 'who',
		 'so', 'them', 'then', 'than', 'into', 'been', 'over', 'more', 'will', 'can', 'this', 'there']
	s = s + [x.capitalize() for x in s]

	parsed_text = filter(lambda w: not w in s,parsed_text)
	diction = dict()

	for word in parsed_text:
		if word.capitalize() in diction:
			diction[word.capitalize()] += 1
		else:
			diction[word.capitalize()] = 1

	sortedLists = []
	problemList = []
	problemTotal = 0
	personalList = []
	personalTotal = 0
	solutionList = []
	solutionTotal = 0

	problem = ['problem', 'problems', 'issue', 'issues', 'dilemma', 'trouble', 'troubles', 'predicament',
				'predicaments', 'obstacle', 'obstacles', 'failure', 'failures']
	personalStory = ['I', 'me', 'my', 'we', 'our', 'ours']
	solution = ['solution', 'solutions', 'mitigate', 'mitigates', 'mitigated', 'resolve', 'resolves', 
				'resolved', 'divert', 'diverts', 'diverted', 'prevent', 'prevents', 'prevented',
				 'solve', 'solves', 'solved', 'help', 'helps', 'helped', 'fix', 'fixes', 'fixed', 'correct',
				 'repair', 'repairs', 'repaired', 'mend', 'mends', 'mended', 'improve', 'improves', 'improved',
				 'rectify', 'rectified', 'stop', 'stops', 'stopped', 'end', 'ends', 'ended']
	searchTerm = nltk.word_tokenize(searchTerm)

	problem = [x.capitalize() for x in problem]
	personalStory = [x.capitalize() for x in personalStory]
	solution = [x.capitalize() for x in solution]
	searchTerm = [x.capitalize() for x in searchTerm]
	allLists = problem + personalStory + solution + searchTerm

	noLists = []

	for  word in sorted(diction, key = diction.get, reverse = True):
		line = (word, diction[word])
		sortedLists.append(line)
		if (word not in allLists):
			noLists.append(word)

	if (len(noLists) < 2):
		noLists = ['', '']
	return [noLists[0], noLists[1]]


def main():
	visible_text = sys.argv[1]
	searchTerm = sys.argv[2]
	bagOfWordsTopTwo(visible_text, searchTerm)

if __name__ == "__main__":
	main()