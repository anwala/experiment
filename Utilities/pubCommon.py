import time
import os, sys
import requests

from random import randint


def randSleep(maxSleepInSeconds=5):

	if( maxSleepInSeconds < 1 ):
		maxSleepInSeconds = 5

	sleepSeconds = randint(1, maxSleepInSeconds)
	print('\trandSleep(): sleep:', sleepSeconds)
	time.sleep(sleepSeconds)

def genericErrorInfo():
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	errorMessage = fname + ', ' + str(exc_tb.tb_lineno)  + ', ' + str(sys.exc_info())
	print('\tERROR:', errorMessage)
	
def getCustomHeaderDict():

	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:38.0) Gecko/20100101 Firefox/38.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'Connnection': 'keep-alive',
		'Cache-Control':'max-age=0'	
	}

	headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'

	return headers

def mimicBrowser(uri, getRequestFlag=True):
	
	uri = uri.strip()
	if( len(uri) == 0 ):
		return ''

	try:
		headers = getCustomHeaderDict()
		response = ''

		if( getRequestFlag ):
			response = requests.get(uri, headers=headers, timeout=10)
			return response.text
		else:
			response = requests.head(uri, headers=headers, timeout=10)
			return response.headers
	except:

		genericErrorInfo()
		print('\tquery is: ', uri)
	
	return ''

def dereferenceURI(URI, maxSleepInSeconds=5):
	
	#print('dereferenceURI():', URI)
	URI = URI.strip()
	if( len(URI) == 0 ):
		return ''
	
	htmlPage = ''
	try:

		'''
			if( debugModeFlag ):
				print('\toffline: reading from output.html')
				infile = open('output.html', 'r')
				htmlPage = infile.read()
				infile.close()
		'''
		
		if( maxSleepInSeconds > 0 ):
			randSleep(maxSleepInSeconds)

		htmlPage = mimicBrowser(URI)
	except:
		genericErrorInfo()
	
	return htmlPage
