import os, sys
import hashlib

#utility - start
def genericErrorInfo():
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	errorMessage = fname + ', ' + str(exc_tb.tb_lineno)  + ', ' + str(sys.exc_info())
	print('\tERROR:', errorMessage)

def readTextFromFile(infilename):

	text = ''
	try:
		infile = open(infilename, 'r')
		text = infile.read()
		infile.close()
	except:
		genericErrorInfo()

	return text

def getURIHash(uri):

	uri = uri.strip()
	if( len(uri) == 0 ):
		return ''

	hash_object = hashlib.md5(uri.encode())
	return hash_object.hexdigest()
#utility - end

def testBoilerplateRM(folderName):

	print('\ntestBoilerplateRM() - start')
	
	boilerplateRMMethodsOutput = ['beautifulsoup.txt', 'clean_html.txt', 'goose.txt', 'justext.txt', 'boilerpipe.ArticleExtractor.txt', 'boilerpipe.DefaultExtractor.txt', 'boilerpipe.CanolaExtractor.txt', 'boilerpipe.LargestContentExtractor.txt', 'python-readability.txt']
	
	goldStandardSet = readTextFromFile(folderName + 'gold-standard.txt')
	goldStandardSet = set(goldStandardSet.split())

	for boilerplateMethod in boilerplateRMMethodsOutput:

		boilMethodSet = set( readTextFromFile(folderName + boilerplateMethod).split() )
		
		intersection = float(len(goldStandardSet & boilMethodSet))
		union = len(goldStandardSet | boilMethodSet)

		score = intersection/union
		print('\tjaccardIndex:', boilerplateMethod, score)
	
	print('testBoilerplateRM() - start\n')

def entryPoint():

	sampleURIs = [
					"http://www.wsj.com/articles/indiana-gives-7-million-in-tax-breaks-to-keep-carrier-jobs-1480608461",
					"http://www.cnbc.com/2016/12/01/howard-schultz-stepping-down-as-starbucks-ceo.html",
					"http://www.usatoday.com/story/news/nation-now/2016/12/01/death-toll-tennessee-wildfires-rises-10/94756844/?utm_source=dlvr.it&utm_medium=twitter",
					"https://www.washingtonpost.com/politics/shouting-match-erupts-between-clinton-and-trump-aides/2016/12/01/7ac4398e-b7ea-11e6-b8df-600bd9d38a02_story.html?utm_term=.f17f35b548b4",
					"http://www.telegraph.co.uk/football/2016/12/01/arsenal-should-glad-efl-cup/",
					"http://nymag.com/thecut/2016/12/victorias-secret-angel-jasmine-tookes-diet-workout-routine.html",
					"http://www.nytimes.com/2016/12/19/world/europe/russia-ambassador-shot-ankara-turkey-report.html",
					"http://www.latimes.com/local/lanow/la-me-san-bernardino-terror-probe-20161130-story.html",
					"http://www.wsj.com/articles/wells-fargo-to-keep-commissions-based-retirement-accounts-under-fiduciary-rule-1480615211",
					"http://www.theatlantic.com/entertainment/archive/2016/12/trevor-noah-finds-his-late-night-voice/509318/"
				]

	shortURIs = [ 'https://archive.is/VWV9j',
				  'https://archive.is/NiUZp',
				  'https://archive.is/sSTDw',
				  'https://archive.is/lhxuj',
				  'https://archive.is/rxvyt',
				  'https://archive.is/SduYw',
				  'https://archive.is/wKOBW',
				  'https://archive.is/l1tqE',
				  'https://archive.is/C0MF6',
				  'https://archive.is/hx6jw'
				  ]

	for uri in sampleURIs:#or shortURIs
		print('uri:', uri)
		testBoilerplateRM('./' + getURIHash(uri) + '/')

entryPoint()