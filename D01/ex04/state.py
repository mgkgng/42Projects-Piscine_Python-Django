import sys

def getKey(v, d) :
	for x, y in d.items() :
		if y == v :
			return x

def state(capital) :
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	if capital in capital_cities.values() :
		print(getKey(getKey(capital, capital_cities), states))
	else :
		print("Unknown capital city")

if __name__ == "__main__":
	if len(sys.argv) != 2 :
		exit(0)
	state(sys.argv[1])