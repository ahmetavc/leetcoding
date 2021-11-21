# https://leetcode.com/problems/3sum/submissions/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            low = i + 1
            high = len(nums) - 1
            
            target = - nums[i]
            
            while low < high:

                if nums[high] + nums[low] < target:
                    low += 1
                
                elif nums[high] + nums[low] > target:
                    high -= 1
                
                else:
                    result.append([nums[i], nums[low], nums[high]])
                    
                    while high > 0 and nums[high - 1] == nums[high]:
                        high -= 1
                        
                    while low < (len(nums) - 1) and nums[low + 1] == nums[low]:
                        low += 1
                        
                    low += 1
                    high -= 1
                        
        return result
                        
                        
                    
                    
                
