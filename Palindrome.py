class Solution():
	def canPermutePalindrome(self, s):
		counter_dic = dict()
		for val in s:
			if val in counter_dic:
				counter_dic[val] += 1
			else:
				counter_dic[val] = 1
		temp_cnt = 0
		for val in counter_dic.values():
			temp_cnt += val%2
			if temp_cnt > 1:
				return False
		return True










test = Solution()
ans = test.canPermutePalindrome("")
print(ans)