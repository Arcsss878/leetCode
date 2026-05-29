class Solution(object):
    def minElement(self, nums):
        #cara efisien
        min_sum = float('inf')
        for num in nums:
            #sbuat simpen angka baru
            s = 0
            n = num
            #selama n bukan nol (n ini nanti nol kalo udah digit trakhir // 10 pasti jadi nol)
            while n:
                #modulo 10 ini ambil digit trakhir, // 10 buat ngapus digit paling blakang
                s += n % 10
                n //= 10
            #kalo sumnya lebih kecil dari min di jadiin nilai terkecil
            if s < min_sum:
                min_sum = s
        return min_sum

        #cara logic
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
        