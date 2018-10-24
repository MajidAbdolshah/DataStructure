import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
            print(nums)

            
        return nums[0]

test = Solution()
ans = test.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print(ans)
