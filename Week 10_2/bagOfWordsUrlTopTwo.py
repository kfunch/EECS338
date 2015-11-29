import sys
import urllib
import urllib2
import json
import nltk
#from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup

def bagOfWordsUrlTopTwo(url, searchTerm):
	hdr = { 'User-Agent' : 'NLP project test' }
	req = urllib2.Request(url, headers=hdr)
	resp = urllib2.urlopen(req)
	html = resp.read()
	soup = BeautifulSoup(html, "lxml")
	[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
	visible_text = soup.find_all('p')
	visible_text1 = ''
	for x in range(0, len(visible_text)):
		visible_text1 = visible_text1 + visible_text[x].getText()
	visible_text = re.sub("[\.\t\,\:;\(\)\.\?\-\]\[\^\'\"\%\|\<\>\+\&\!]", "", visible_text1, 0, 0)
	parsed_text = nltk.word_tokenize(visible_text)

	s = ['the', 'of', 'a', 'an', 'and', 'to', 'that', 'in', 'is', 'as', 'for', 'it', 'with', 'on', 'was', 'be', 'at',
		 'by', 'on', 'out', 'has', 'have', 'he', 'she', 'him', 'her', 'they', 'are', 'not', 'all', 'what',
		 'would', 'but', 'or', 'their', 'from', 'like', 'had', 'about', 'which', 'were', 'just', 'if', 'when', 'who',
		 'so', 'them', 'then', 'than', 'into', 'been', 'over', 'more', 'will', 'can', 'this', 'there', 'you',
		 'no']
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
		# line = (word, diction[word])
		# sortedLists.append(line)
		# if (word in solution):
		# 	solutionList.append(line)
		# 	solutionTotal = solutionTotal + diction[word]
		# if (word in problem):
		# 	problemList.append(line)
		# 	problemTotal = problemTotal + diction[word]
		# if (word in personalStory):
		# 	personalList.append(line)
		# 	personalTotal = personalTotal + diction[word]
		if (word not in allLists):
			noLists.append(word)

	if (len(noLists) < 2):
		noLists = ['', '']
	return [noLists[0], noLists[1]]


def main():
	url = sys.argv[1]
	searchTerm = sys.argv[2]
	bagOfWordsUrlTopTwo(url, searchTerm)

if __name__ == "__main__":
	main()