import numpy as np


def findsolution(str_):
	return numways(str_,len(str_))

def numways(str_,k):

	#print('__K__')
	#print(k)


	if (k==0):
		return 1
	start_ = len(str_)-k
	#print('start_')
	#print(str_[start_:])
	if (str_[start_]=='0'):
		return 0
	flag = 1
	if (int(str_[start_:start_+2]) <= 26) and (k>=2):
		flag = 2

	if (flag == 2):
			result = numways(str_,k-1)+numways(str_,k-2)
	else:
			result = numways(str_,k-1)
	
	
	return result

string = "10023"
res_ = findsolution(string)
print(res_)