import numpy as np


hTable = {}
counter_ = 0

def fFunc(n):
	global counter_
	counter_+=1
	if (n in hTable):
		return hTable[n]
	if (n<=2):
		return 1
	else:
		hTable[n] = fFunc(n-1)+fFunc(n-2)

	return hTable[n]

print(fFunc(6))
print(counter_)