class Solution():
	def anagramMappings(self, A, B):
		indX = []
		for val in A:
			indX.append(B.index(val))
		return indX

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
test = Solution()
ans = test.anagramMappings(A,B)
print(ans)
