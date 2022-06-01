import sys

def capital_city(state_name) :
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
	if state_name in states.keys():
		print(capital_cities[states[state_name]])
	else :
		print("Unknown state")

if __name__ == "__main__" :
	if len(sys.argv) != 2 :
		exit(0)
	capital_city(sys.argv[1])