import numpy as np 

str_1 = "TOFOODIE"
str_2 = "TOODY"

s_1 = len(str_1)+1
s_2 = len(str_2)+1

Memo = np.zeros(shape=(s_1,s_2))

for i in range(1,s_1):
	for j in range(1,s_2):
		if str_1[i-1] == str_2[j-1]:
			Memo[i,j] = Memo[i-1,j-1] + 1

print(Memo)


