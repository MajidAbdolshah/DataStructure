import numpy as np


def findsolution(str_,Memo):
	return numways(str_,len(str_),Memo)

def numways(str_,k,Memo):

	print('__K__')
	print(k)

	if k in Memo:
		return Memo[k]

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
			result = numways(str_,k-1,Memo)+numways(str_,k-2,Memo)
	else:
			result = numways(str_,k-1,Memo)
	
	Memo[k] = result
	print(Memo)
	return result

string = "123"
Memo = {}
res_ = findsolution(string,Memo)
