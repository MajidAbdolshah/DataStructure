import numpy as np


hTable = {}
counter_ = 0

def fFunc(n):
	global counter_
	counter_+=1
	#if (n in hTable):
    #	return hTable[n]
	if (n<=2):
		return 1
	else:
		Res = fFunc(n-1)+fFunc(n-2)

	return Res

print(fFunc(6))
print(counter_)