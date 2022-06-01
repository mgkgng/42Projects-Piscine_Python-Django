import sys

def parse(l):
	res = list()
	for i in l:
		if len(i.strip()) > 0:
			res.append(i.strip())
	return (res)

def getKey(v, d) :
	for x, y in d.items() :
		if y == v :
			return x

def is_state(name, d) :
	for elem in d.keys():
		if name.lower() == elem.lower():
			return elem
	return "Unknown"

def is_capital(name, d) :
	for elem in d.values():
		if name.lower() == elem.lower():
			return elem
	return "Unknown"

def all_in(lst):
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

	if len(lst) == 0:
		return
	for i in lst:
		if len(i) == 0:
			continue
		if is_state(i, states) != "Unknown":
			name = is_state(i, states)
			print(capital_cities[states[name]] + " is the capital of " + name)
		elif is_capital(i, capital_cities) != "Unknown":
			name = is_capital(i, capital_cities)
			print(name + " is the capital of " + getKey(getKey(name, capital_cities), states))
		else:
			print(i + " is neither a capital nor a state")

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		exit(0) 
	all_in(parse(sys.argv[1].split(",")))