def showNbs(file) :
	content = open(file, 'r').read().split(",")
	for n in content:
		print(n)

if __name__ == '__main__' :
	showNbs("numbers.txt")