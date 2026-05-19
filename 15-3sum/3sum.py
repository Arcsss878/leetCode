class Solution(object):
    def threeSum(self, nums):
        #Sorting nums dulu supaya bisa di pointer
        nums.sort()
        hasil = []
        #buat loop (nomor pertama (i)- angka yang sibutuhkan setelahnya) karena kita butuh 3 angka jadi kalo udah sampe -3 masih punya -2 -1 buat pembanding
        for i in range(len(nums) - 2):
            #skip duplikat nomor sebelumnya kalo ada jadi mempercepat loop(kalo duplikat sol bakal sama)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #initialisasi left(angka ke 2), right (ujung kanan), dan target(angka i butuh brapa biar jadi nol)
            left = i + 1
            right = len(nums) - 1
            target = -nums[i]
            #selama kiri belum lewati kanan
            while left < right:
                curr_sum = nums[left] + nums[right]
                #bandingin jum angkanya
                if curr_sum == target:
                    #sama ya tambahin aja hasilnya
                    hasil.append([nums[i], nums[left], nums[right]])
                    #kurangi kanan kiri langsung biar lanjut bandingin i sama kombinasi lain
                    left += 1
                    right -= 1
                    #ini dicek in kalo angkanya duplikat ato ga, semisal duplikat langsung digeser lagi biar mempercepat kalo ga ya skip whilenya ini
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif curr_sum < target:
                    #kalo kurang left tambah(angka membesar)
                    left += 1
                else :
                    #kalo lebih right kurang(angka mengecil)
                    right -= 1
        return hasil
            
        