class Arithmetic:
	def __init__(self, num1, num2):
		self.num1=num1
		self.num2=num2
		
	def add(self):
		return self.num1+self.num2

	def sub(self):
		return self.num1-self.num2

	def mult(self):
		return self.num1*self.num2

	def divide(self):
		if self.num1==0 or self.num2==0:
			return "Can't divide by 0"

a1=Arithmetic(20,60)
print(f" addition of numbers are : {a1.add()}")
print(f"Subtraction of given number is :{a1.sub()}")