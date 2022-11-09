def add(*args):
	result = 0
	for n in args:
		result += n
	return result



print(add(50,20,10,20,30,70,28))


def calculate(n, **kwargs):
	print(kwargs)
	n += kwargs["add"]
	n *= kwargs["multiply"]
	print(n)


calculate(2, add=3, multiply=5)


class Car:
	def __init__(self, **kwargs):
		self.make = kwargs.get("make")
		self.model = kwargs.get("model")
		self.engine = kwargs.get("engine")
		self.trim = kwargs.get("trim")
		self.color = kwargs.get("color")
		self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.trim)	#returns None