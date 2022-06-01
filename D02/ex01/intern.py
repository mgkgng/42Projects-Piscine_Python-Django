class Intern :
	def __init__(self, name = "My name? I’m nobody, an intern, I have no name.")
		self.Name = name

	def	__str__(self):
		pass

	class Coffee:
		def __str__(self):
			pass

	def	work(self):
		raise Exception("I’m just an intern, I can’t do that...")
	
	def make_coffee(self):
		return Intern.Coffee()

if __name__ == "__main__":
	mark = Intern("Mark")