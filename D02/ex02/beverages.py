class HotBeverage:
	price = 0.30
	name = "hot beverage"

	def description(self):
		return "Just some hot water in a cup."
	
	def __str__(self):
		return "name : " +  self.name + "\n" + "price : " +  str(self.price) + "\n" + "description : " + self.description() + "\n"


class Coffee(HotBeverage):
	price = 0.40
	name = "coffee"

	def description(self):
		return "A coffee, to stay awake."


class Tea(HotBeverage):
	price = 0.30
	name = "tea"

	def description(self):
		return "Just some hot water in a cup."

class Chocolate(HotBeverage):
	price = 0.50
	name = "chocolate"

	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	price = 0.45
	name = "cappuccino"

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