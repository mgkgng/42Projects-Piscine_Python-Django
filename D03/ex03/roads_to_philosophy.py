import sys, requests
from bs4 import BeautifulSoup

def check_strErr(str):
	if str.find(' ') != -1:
		print("Error: Space found")
		exit(0)

def route_wiki(route):
	S = requests.Session()

	URL = "https://en.wikipedia.org" + route

	#R = S.get(url=URL, params=PARAMS)
	#DATA = R.json()
	R = S.get(url=URL)
	if R.status_code == 404:
		print("It's a dead end !")
		exit(0)
	DATA = R.content

	soup = BeautifulSoup(DATA, 'html.parser')
	#print(soup.prettify())
	#for line in soup.find_all(class_="thumb tright"):
		#line.extract()
	#for table in soup.find_all("table"):
		#table.extract()
	#for e in soup.find_all("a", class_=True):
		#e.extract()
	#for e in soup.find_all("a", id=True):
		#e.extract()
	#for e in soup.find_all("img"):
		#e.extract()
	#for e in soup.find_all("span"):
		#e.extract()
	for e in soup.find_all("a"):
		if e.parent.name != "p":
			e.extract()
	list = soup("a")
	if len(list) == 0:
		print("It's a dead end !")
		exit(0)
	#for e in list:
	#	print(e)
	return list[0]

def	write_file(filename, str):
	fileW = open(filename + ".wiki", 'w')
	fileW.write(str)
	fileW.close()


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Error: Wrong number of arguments.")
		exit(0)
	road = [sys.argv[1]]
	done = False
	word = route_wiki("/wiki/" + str(sys.argv[1]).replace(' ', '_'))
	while done == False:
		name = word.attrs["title"]
		link = word.attrs["href"]
		if name in road:
			for e in road:
				print(e)
			print("It leads to an infinite loop!")
			exit(0)
		road.append(name)
		if name == "Philosophy":
			done = True
			break
		word = route_wiki(link)

	for e in road:
		print(e)
	print(f"{len(road)} roads from {sys.argv[1]} to philosophy!")
