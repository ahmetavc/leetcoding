#https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return self.divideAndConquer(nums, 0, len(nums)-1)
        
        
    def divideAndConquer(self, nums, low, high):
        if low == high:
            return nums[low]
        
        mid = (low + high) // 2
        
        lowMax = self.divideAndConquer(nums, low, mid)
        highMax = self.divideAndConquer(nums, mid+1, high)
        crossMax = self.findCrossMax(nums, low, high, mid)
        
        return max(lowMax, highMax, crossMax)
    
    def findCrossMax(self, nums, low, high, mid):
        leftMax = nums[mid]
        leftMin = nums[mid]
        cur = nums[mid]
        
        for i in range(mid-1, low-1, -1):
            cur *= nums[i]
            
            if cur > leftMax:
                leftMax = cur
            
            if cur < leftMin:
                leftMin = cur
                
        rightMax = nums[mid+1]
        rightMin = nums[mid+1]
        cur = nums[mid+1]
        
        for i in range(mid+2, high+1):
            cur *= nums[i]
            
            if cur > rightMax:
                rightMax = cur
                
            if cur < rightMin:
                rightMin = cur
        
        return max(leftMax*rightMax, leftMin*rightMin)
        
