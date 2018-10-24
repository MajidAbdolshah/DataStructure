class Solution(object):
	def isPerfectSquare(self, num):
		left = 1
		right = num

		if num == 1 or num == 0:
			return True
		while left < right:
			mid = (left+right)//2
			if mid**2 > num:
				right = mid-1
			elif mid**2 < num:
				left = mid + 1
			else:
				return True
		return False

test = Solution()
print(test.isPerfectSquare(15))

