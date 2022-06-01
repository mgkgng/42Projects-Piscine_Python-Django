def showNbs(file) :
	content = open(file, 'r').read().split(",")
	for e in content:
		print(e.rstrip("\n"))

if __name__ == '__main__' :
	showNbs("numbers.txt")