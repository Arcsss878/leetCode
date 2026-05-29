class Solution(object):
    def minElement(self, nums):
        min_sum = float('inf')
        for num in nums:
            s = 0
            n = num
            while n:
                s += n % 10
                n //= 10
            if s < min_sum:
                min_sum = s
        return min_sum
        #declare yang terkecil dulu, kasik infinite biar semuanya lebih kecil
        smallest = float('inf')
        #iterasi setiap isinya
        for i in nums:
            #itu jumlah angka, fornya ini nanti nge jumlahin angka hasil iterasi semua string di i
            dig_sum = sum(int(d) for d in str(i))
            #kalo angkanya sekarang lebih kecil smallest di benerin
            if dig_sum < smallest:
                smallest = dig_sum
        return smallest
        