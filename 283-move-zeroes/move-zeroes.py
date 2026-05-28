class Solution(object):
    def moveZeroes(self, nums):
        insert = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert] = nums[i]
                insert += 1
        nums[insert:] = [0] * (len(nums) - insert)
        return nums
        