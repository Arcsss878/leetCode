class Solution(object):
    def numberOfSpecialChars(self, word):
        huruf = set()
        total = 0
        for i in word:
            huruf.add(i)
        for c in string.ascii_lowercase:
            if c in huruf and c.upper() in huruf:
                total += 1
        return total
        