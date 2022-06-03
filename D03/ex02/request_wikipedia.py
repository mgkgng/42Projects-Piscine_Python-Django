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

	PAGES = DATA["query"]["pages"]
	#print(json.dumps(PAGES, sort_keys=True, indent=4))
	return dewiki.from_string(PAGES[0]["revisions"][0]["slots"]["main"]["content"])

def	write_file(filename, str):
	fileW = open(filename + ".wiki", 'w')
	fileW.write(str)
	fileW.close()

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Error: Wrong number of arguments.")
		exit(0)
	write_file(sys.argv[1], request_wiki(sys.argv[1]))