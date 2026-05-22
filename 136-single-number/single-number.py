class Solution(object):
    def singleNumber(self, nums):
        #jadi ni pake xor, xor sendriri mbandingin bit perbit dari angkanya itu. ini works karena kalo angkanya sama hasilnya pasti nol tapi kalo angka biasa sama nol hasilnya angka itu sendiri(makanya mulai dari nol). karena XOR ini komutatif jadi angka pair nanti bakal saling cancel out sisain angka yang ga ada pairnya
        #contoh : 4 ^ 1 ^ 2 ^ 1 ^ 2 = (1 ^ 1) ^ (2 ^ 2) ^ 4 = 0 ^ 0 ^ 4 = 4.
        result = 0
        for num in nums:
            result ^= num
        return result

        #other solution (di persingkat aja)
        #reduce ini fungsi yang ambil 2 input tapi balikin 1 input, lambanya buat deklarasi fungsi XOR. Nanti reducenya bakal eksekusi lambda dari ngambil angka dari nums di parameter kedua
        return reduce(lambda x, y: x ^ y, nums)

        #solusi pake dictionary
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            if c == 1:
                return n
        