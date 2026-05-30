class Solution(object):
    def missingNumber(self, nums):
        res = 0
        for i in range(len(nums)):
            res ^= i+1
            res ^= nums[i]
        return res
        
        