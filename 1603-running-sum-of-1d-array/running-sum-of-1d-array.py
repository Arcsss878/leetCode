class Solution(object):
    def runningSum(self, nums):
        curr_sum = 0
        r = []
        for i in nums:
            curr_sum += i
            r.append(curr_sum)
        return r
        