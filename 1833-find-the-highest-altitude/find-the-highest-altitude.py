class Solution(object):
    def largestAltitude(self, gain):
        cur = 0
        high = 0
        for i in gain:
            cur += i
            high = max(high, cur)
        return high
        