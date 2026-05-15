class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        ori = x
        r = 0
        while x > 0:
            digit = x % 10
            r = (r * 10) + digit
            x = x // 10
            
        return ori == r