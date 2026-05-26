class Solution(object):
    def longestPalindrome(self, s):
        letter = Counter(s)
        total = 0
        ganjil = False
        for count in letter.values():
            temp = count % 2
            if temp == 0:
                total += count
            else:
                ganjil = True
                total += count - 1
        if ganjil == True:
            return total + ganjil
        else :
            return total
        