import random
from beverage import HotBeverage, Cappuccino, Tea, Coffee, Chocolate

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

	def repair(self):
		self.broken = False
		self.served = 0

	def serve(self, drink):
		if self.broken == True:
			raise self.BrokenMachineException
		self.served += 1
		if self.served > 9:
			self.broken = True
		return drink() if random.random() < 0.5 else self.EmptyCup()
	
	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__(self, "This coffee machine has to be repaired.")

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(1, 6):
		print(f"======={i}time=======")
		print(str(machine.serve(Cappuccino)))
	for i in range(6, 11):
		print(f"======={i}time=======")
		print(str(machine.serve(Tea)))
	print(f"=======11time=======")
	try:
		print(str(machine.serve(Coffee)))
	except machine.BrokenMachineException as e:
		print(e)
	machine.repair()
	print(f"=======12time=======")
	print(str(machine.serve(Chocolate)))

	