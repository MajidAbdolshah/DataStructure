import numpy as np

class Queue():

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return (len(self.items) == 0)

	def Que(self,x):
		self.items.insert(0,x)

	def Dque(self):
		if not self.isEmpty():
			self.items.pop()
		else:
			print('list is empty!')
			return -1

	def Peek(self):
		return self.items[0]

	def Print(self):
		print(self.items)

def main():
	
	Q_ = Queue()
	Q_.Print()
	Q_.Que(3)
	Q_.Que(5)
	Q_.Que(7)
	Q_.Que(9)
	Q_.Que(11)
	Q_.Print()
	Q_.Dque()
	Q_.Print()
	Q_.Dque()
	Q_.Print()
	Q_.Dque()
	Q_.Print()
	Q_.Dque()
	Q_.Print()
	Q_.Dque()
	Q_.Print()
	Q_.Dque()
	
	
if __name__ == "__main__":
	main()

