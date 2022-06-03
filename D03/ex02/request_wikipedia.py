import requests, sys, json
import dewiki


def check_strErr(str):
	if str.find(' ') != -1:
		print("Error: Space found")
		exit(0)

def request_wiki(filename):
	S = requests.Session()
	URL = "https://en.wikipedia.org/w/api.php"

	PARAMS = {
		"action": "query",
		"prop": "revisions",
		"titles": filename,
		"rvprop": "content",
		"rvslots": "main",
		"formatversion": "2",
		"format": "json",
		"redirects": "1"
	}

	R = S.get(url=URL, params=PARAMS)
	DATA = R.json()
	#print(json.dumps(DATA, sort_keys=True, indent=4))
	#if missing == True
		#return "Couldn't find " + filename + " on Wikipedia!"

	PAGES = DATA["query"]["pages"]
	#print(json.dumps(PAGES, sort_keys=True, indent=4))
	
	res = PAGES[0]["revisions"][0]["slots"]["main"]["content"]
	test = dewiki.from_string(res)
	
	print(test)
	return res

def	write_file(filename, str):
	fileW = open(filename + ".wiki", 'w')
	fileW.write(str)
	fileW.close()


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Error: Wrong number of arguments.")
		exit(0)
	write_file(sys.argv[1], request_wiki(sys.argv[1]))