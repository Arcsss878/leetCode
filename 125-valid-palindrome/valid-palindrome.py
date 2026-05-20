class Solution(object):
    def isPalindrome(self, s):
        text = ''.join(char for char in s if char.isalnum()).lower()
        left = 0
        right = len(text) - 1
        while left < right:
            if text[left] == text[right]:
                left += 1
                right -=1
                continue
            else:
                return False
        return True
