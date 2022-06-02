from inspect import getmembers
import sys, os, re
import settings

def checkError(argv):
	if len(argv) != 2:
		exit(0)
	if sys.argv[1][-9:] != ".template" or len(argv[1]) < 10:
		print("coucou")
		exit(0)

def getValues():
	l = getmembers(settings)
	for i in range(8):
		l.pop(0)
	res = dict()
	for elem in l:
		res[elem[0]] = elem[1]
	return res

def getVariables(line):
	return re.findall('{.*?}', line)

def getReplace(str, values):
	if str not in values.keys():
		print(f"Error: variable '{str}' not found in settings")
		exit(1)
	return values[str]

def	render(file):
	src = open(file, 'r').readlines()
	dest = open(file[:-9] + ".html", 'w')
	values = getValues()
	for line in src:

		toRender = getVariables(line)
		if len(toRender) != 0:
			for elem in toRender:
				line = line.replace(elem, str(getReplace(elem.lstrip('{').rstrip('}'), values)))
		dest.write(line)
	dest.close()

if __name__ == "__main__":
	#checkError(sys.argv)
	render(sys.argv[1])