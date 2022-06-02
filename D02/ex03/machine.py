import random
from beverage import HotBeverage, Cappuccino

class CoffeeMachine():
	served = 0
	broken = False

	def __init__(self):
		pass
	
	class EmptyCup(HotBeverage):
		price = 0.90
		name = "empty cup"

		def description(self):
			return "An empty cup?! Gimme my money back!"
	
	class BrokenMachineException(Exception):
		def __init__(self):
			pass
		#"This coffee machine has to be repaired."

	def repair(self):
		self.broken = False
		self.served = 0

	def serve(self, drink):
		if self.broken == False:
			raise self.BrokenMachineException()
		self.served += 1
		if self.served > 9:
			self.broken = True
		return drink() if random.random < 0.5 else self.EmptyCup
