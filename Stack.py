import numpy as np

class Stack():
	
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return (len(self.items) == 0)

	def Push(self,x):
		self.items.append(x)

	def Pop(self):
		if not self.isEmpty():
			return self.items.pop()
		else:
			return -1

	def Peek(self):
		return self.items[-1]

	def Size(self):
		return len(self.items)

	def Print(self):
		print(self.items)

def main():
	
	S_ = Stack()
	S_.Print()
	S_.Push(2)
	S_.Push(5)
	S_.Push(7)
	S_.Print()
	S_.Pop()
	S_.Print()
	S_.Pop()
	S_.Print()
	S_.Push(10)
	print(S_.Peek())
	S_.Print()

if __name__ == "__main__":
	main()


