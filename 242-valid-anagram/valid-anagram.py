class Solution(object):
    def isAnagram(self, s, t):
        #pakai sorted(), nanti dirapiin terus di bandingin
        return sorted(s) == sorted (t)
        