import sys
import urllib
import urllib2
import json
import nltk
#from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup

def findSentence(url, searchTerm, sentencePt1, sentencePt2):
	hdr = { 'User-Agent' : 'NLP project test' }
	req = urllib2.Request(url, headers=hdr)
	resp = urllib2.urlopen(req)
	html = resp.read()
	soup = BeautifulSoup(html, "lxml")

	visible_text = []
	clean_text = []
	paragraphs = soup.find_all('p')
	for x in range(0, len(paragraphs)):
		visible_text.append(paragraphs[x].getText())
		clean_text.append(re.sub("[\.\t\,\:;\(\)\.\?\-\]\[\^\'\"\%\|\<\>\+\&]", "", visible_text[x], 0, 0))

	paragraphArr = []
	cleanParagraphArr = []

	for x in range(0, len(clean_text)):

		regEx = sentencePt1 + searchTerm + sentencePt2
		found = re.search(regEx.lower(), clean_text[x].lower())
		if found:
			paragraphArr.append(visible_text[x])
			cleanParagraphArr.append(clean_text[x])

	return [paragraphArr, cleanParagraphArr]

def main():
	url = sys.argv[1]
	searchTerm = sys.argv[2]
	findSentence(url, searchTerm)

if __name__ == "__main__":
	main()