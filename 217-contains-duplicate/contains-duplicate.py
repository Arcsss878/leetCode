class Solution(object):
    def containsDuplicate(self, nums):
        seen = {}
        for val in nums:
            if val in seen:
                return True
            seen[val] = True
        return False
        