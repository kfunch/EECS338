import sys
import urllib
import urllib2
import json
import nltk
#from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup
import cookielib
import httplib
import socket

def findSentence(url, searchTerm, sentencePt1, sentencePt2, includeSearchTerm):
	try:
		user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
		#hdr = { 'User-Agent' : 'NLP project test' }
		hdr = { 'User-Agent' : 'Mozilla/5.0' }

		#req = urllib2.Request(url, headers=hdr)
		#resp = urllib2.urlopen(req)

		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		req = urllib2.Request(url, headers=hdr)
		resp = opener.open(req)

		html = resp.read()
		soup = BeautifulSoup(html, "lxml")

		visible_text = []
		clean_text = []
		paragraphs = soup.find_all('p')
		for x in range(0, len(paragraphs)):
			regExRemoved = re.sub(r'\<[^\>]*\>', ' ', paragraphs[x].getText())
			regExRemoved = re.sub(r'\[[^\]]*\]', ' ', regExRemoved)
			regExRemoved = re.sub(r'\([^\)]*\)', ' ', regExRemoved)
			visible_text.append(regExRemoved)
			clean_text.append(re.sub("[\.\t\,\:;\(\)\.\?\-\]\[\^\'\"\%\|\<\>\+\&]", "", visible_text[x], 0, 0))

		paragraphArr = []
		searchTermParArr = []
		cleanParagraphArr = []
		cleanSearchTermParArr = []

		for x in range(0, len(clean_text)):
			if (len(clean_text[x]) > 100) and (len(clean_text[x]) < 1000):
				if (includeSearchTerm):
					regEx = sentencePt1 + searchTerm + sentencePt2
					found = re.search(regEx.lower(), clean_text[x].lower())
					if found:
						paragraphArr.append(visible_text[x])
						cleanParagraphArr.append(clean_text[x])
				else:
					regEx = sentencePt1
					#regEx = sentencePt1 + sentencePt2
					if (re.search(searchTerm.lower(), clean_text[x].lower())):
						if (re.search(regEx.lower(), clean_text[x].lower())):
							paragraphArr.append(visible_text[x])
							cleanParagraphArr.append(clean_text[x])
						else:
							searchTermParArr.append(visible_text[x])
							cleanSearchTermParArr.append(clean_text[x])

		if (len(paragraphArr) < 1):
			return [searchTermParArr, cleanSearchTermParArr, 0]
		else:
			return [paragraphArr, cleanParagraphArr, 1]

	except (httplib.BadStatusLine, urllib2.HTTPError, socket.error, urllib2.URLError) as e:
		return [[], [], 0]

def main():
	url = sys.argv[1]
	searchTerm = sys.argv[2]
	findSentence(url, searchTerm)

if __name__ == "__main__":
	main()