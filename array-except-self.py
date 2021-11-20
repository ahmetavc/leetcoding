# https://leetcode.com/problems/product-of-array-except-self/submissions/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        
        for i in range(1, length):
            res[i] = res[i-1] * nums[i-1]
            
        right = 1
            
        for i in range(length - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
            
        return res
