import sys

def checkError(argv):
	if len(argv) != 3:
		exit(0)
	if sys.argv[1][-9:] != ".template" or len(argv[1]) < 10:
		exit(0)

def	render(file):
# remplacer {variable_name} en valeur ecrit en myCV.template
	pass

if __name__ == "__main__":
	checkError(sys.argv)
	render(sys.argv[1])