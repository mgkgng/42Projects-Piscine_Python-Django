from local_lib.path import Path

if __name__ == "__main__":
	p = Path("./piscineDjango")
	try:
		p.mkdir(0o666)
	except Exception as e:
		print(e)
	filepath = str(p) + "/file"
	print(filepath)
	fileW = open(filepath, 'w')
	fileW.write("Exercice succeeded.")
	fileW.close()
	fileR = open(filepath, 'r')
	print(fileR.read())
	fileR.close()