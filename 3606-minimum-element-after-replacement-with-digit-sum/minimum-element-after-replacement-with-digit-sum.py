class Solution(object):
    def minElement(self, nums):
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
        