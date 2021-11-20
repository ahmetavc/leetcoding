# https://leetcode.com/problems/maximum-subarray/

class Solution:
# divideAndConquer solution
    def maxSubArray(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        return self.divideAndConquer(nums, 0, len(nums) - 1)
        
        
    def divideAndConquer(self, nums, low, high):
        if low == high:
            return nums[low]
        
        mid = (low + high) // 2
        
        leftSum = self.divideAndConquer(nums, low, mid)
        rightSum = self.divideAndConquer(nums, mid + 1, high)
        crossSum = self.findMaxCrossingSubArray(nums, low, high, mid)
        
        return max(leftSum, rightSum, crossSum)
        
        
    def findMaxCrossingSubArray(self,nums, low, high, mid):
        leftSum = float('-inf')
        sumSoFar = 0
        
        for i in range(mid, low - 1, -1):
            sumSoFar += nums[i]
            
            if sumSoFar > leftSum:
                leftSum = sumSoFar
                
        rightSum = float('-inf')
        sumSoFar = 0
        
        for i in range(mid+1, high + 1):
            sumSoFar += nums[i]
            
            if sumSoFar > rightSum:
                rightSum = sumSoFar

        return leftSum + rightSum
        
        
# basic O(n) solution
        
        
#         maxSoFar = float('-inf')
#         cur = 0
        
#         for num in nums:
#             if cur + num < 0:
#                 if num > maxSoFar:
#                     maxSoFar = num
#                 cur = 0
#                 continue
            
#             cur += num
            
#             if cur > maxSoFar:
#                 maxSoFar = cur
        
#         return maxSoFar
