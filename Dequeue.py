import numpy as np

class DeQueue():

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return (len(self.items)==0)

	def addFront(self,x):
		self.items.insert(0,x)

	def addRear(self,x):
		self.items.append(x)

	def remFront(self):
		self.items.pop(0)

	def remRear(self):
		self.items.pop()

	def Size(self):
		return len(self.items)

	def Peek(self):
		return self.items[0],self.items[-1]

	def Print(self):
		print(self.items)

def main():

	DQ_ = DeQueue()
	DQ_.Print()
	DQ_.addFront(3)
	DQ_.addFront(5)
	DQ_.addFront(7)
	DQ_.Print()
	DQ_.addRear(-1)
	DQ_.addRear(-2)
	DQ_.addRear(-3)
	DQ_.Print()
	DQ_.remRear()
	DQ_.remFront()
	DQ_.Print()

if __name__ == "__main__":
	main()