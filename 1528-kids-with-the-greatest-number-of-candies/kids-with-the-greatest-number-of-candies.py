class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        #buat most buat nampung brapa permen terbanya, r buat result
        most = max(candies)
        r = []
        #cari brapa candy terbanyaknya
        #for i in candies:
        #    most = max(most, i)
        #bandingin candy terbanyak smaa candy dipunya + extra kalo >= true kalo ga false
        for i in candies:
            candy = i + extraCandies
            if  candy >= most:
                r.append(True)
            else:
                r.append(False)
        return r

        #versi singkat
        most = max(candies)
        return [candy + extraCandies >= most for candy in candies]

        