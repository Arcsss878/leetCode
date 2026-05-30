class Solution(object):
    def missingNumber(self, nums):
        #kita pake logic XOR disini buat cancel out angka kembar
        #di kasus ini angkanya urut dari satu sampe n cuman angka hilangnya di ganti nol, angkanya ini nanti bisa di cek dengan xor dari 1 - n nanti saling cancel out dan sisa angka yang hilang

        #buat res untuk menyimpan hasil XOR (XOR ini kalo misal angka yang sama bakal return 0 )
        res = 0
        #kita fornya pake indexing aja biar bisa sekalian ngecek
        for i in range(len(nums)):
            #disini kita langsung aja XOR dari 1 sama isi nums[1] sampe n untuk keduanya
            res ^= i+1
            res ^= nums[i]
        #kembalikin hasilnya
        return res
        
        