from local_lib.path import Path

if __name__ == "__main__":
	p = Path("piscineDjango")
	try:
		p.mkdir()
	except Exception as e:
		print(e)
	s = Path("piscineDjango/file")
	s.touch()
	s.write_text("Exercice succeeded.")
	txt = s.read_text()
	print(txt)