class HotBeverage:
	price = 0.30
	name = "hot beverage"

	def __init__(self):
		pass

	def description(self):
		return "Just some hot water in a cup."
	
	def __str__(self):
		return "name : " +  self.name + "\n" + "price : " +  f"{self.price:.2f}" + "\n" + "description : " + self.description() + "\n"

class Coffee(HotBeverage):
	price = 0.40
	name = "coffee"

	def __init__(self):
		pass

	def description(self):
		return "A coffee, to stay awake."

class Tea(HotBeverage):
	name = "tea"
	
	def __init__(self):
		pass

class Chocolate(HotBeverage):
	price = 0.50
	name = "chocolate"

	def __init__(self):
		pass

	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	price = 0.45
	name = "cappuccino"

	def __init__(self):
		pass

	def description(self):
		return "Un po' di Italia nella sua tazza!"

if __name__=="__main__":
	hotbeverage = HotBeverage()
	coffee = Coffee()
	tea = Tea()
	chocolate = Chocolate()
	cappuccino = Cappuccino()

	print(hotbeverage.__str__())
	print(coffee.__str__())
	print(tea.__str__())
	print(chocolate.__str__())
	print(cappuccino.__str__())