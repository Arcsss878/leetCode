class Solution(object):
    def moveZeroes(self, nums):
        zero = 0
        while 0 in nums:
            nums.remove(0)
            zero += 1
        return nums.extend([0]* zero)
        