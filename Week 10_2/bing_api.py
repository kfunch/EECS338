import urllib
import urllib2
import json
 
def main():
    query = raw_input('Query: ')
    bing_api(query)

def bing_api(query):
    keyBing = ''        # get Bing key from: https://datamarket.azure.com/account/keys
    credentialBing = 'Basic ' + (':%s' % keyBing).encode('base64')[:-1] 
    query = query.replace('\"', '%22')
    searchString = '%27' + query.replace(' ', '+') + '%27'
    top = 10
    offset = 0

    url = 'https://api.datamarket.azure.com/Bing/Search/Web?' + \
          'Query=%s&$top=%d&$skip=%d&$format=json' % (searchString, top, offset)

    request = urllib2.Request(url)
    request.add_header('Authorization', credentialBing)
    requestOpener = urllib2.build_opener()
    response = requestOpener.open(request) 

    results = json.load(response)
    return results

if __name__ == "__main__":
    main()