class Solution(object):
    def containsDuplicate(self, nums):
        seen = {}
        for i, val in enumerate(nums):
            if val in seen:
                return True
            seen[val] = i
        return False
        