class Solution(object):
    def containsDuplicate(self, nums):
        #seen = {}
        #for val in nums:
        #    if val in seen:
        #        return True
        #    seen[val] = True
        #return False

        #pakai set(), set ini langsung ilangin duplikat 
        #jadi kalo ukuran beda pasti ada duplikat
        return len(nums) != len(set(nums))
        