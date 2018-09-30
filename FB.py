import numpy as np


def findCodes(str_):
	result = []
	s_str = len(str_)
	for i in range(s_str):
		result.append(str_[i])
	for i in range(s_str-1):
		result.append([str_[i],str_[i+1]])
	return result




num = 132
snum = str(num)
listnum = list(snum)
print(listnum)

labels = findCodes(listnum)
print(labels)