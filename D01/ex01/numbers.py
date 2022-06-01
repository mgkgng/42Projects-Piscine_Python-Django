def showNbs(file) :
	content = open(file, 'r').read().split(",")
	print(*content, sep='\n')

if __name__ == '__main__' :
	showNbs("numbers.txt")