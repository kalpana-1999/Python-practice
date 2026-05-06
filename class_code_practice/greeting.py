class Calculator:
	def __init__(self, num1,num2):
		self.num1=num1
		self.num2=num2

	def add(self):
		return self.num1+self.num2

	def sub(self):
		return self.num1-self.num2

	def mult(self):
		return self.num1*self.num2

	def divide(self):
		return self.num1/self.num2 if self.num1 and self.num2 >0 else print("Can't divide")

c1=Calculator(23,0)
print(c1.add())
print(c1.sub())
print(c1.mult())
print(c1.divide())
