class Solution(object):
    def firstUniqChar(self, s):
        arr = [0] * 26
        for i in s:
            index = ord(i) - ord('a')
            arr[index] += 1
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if arr[index] == 1:
                return i
        return -1