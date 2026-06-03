class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        most = 0
        r = []
        for i in candies:
            most = max(most, i)
        for i in candies:
            candy = i + extraCandies
            if  candy >= most:
                r.append(True)
            else:
                r.append(False)
        return r


        