class Solution(object):
    def intersection(self, nums1, nums2):
        #cara cepet
        return list(set(nums1) & set(nums2))
        #cara normal
        seen = {}
        hasil = []
        #set dictionary dulu pake satu array
        for num in nums1:
            seen[num] = True
        #di loopnya ini cuman ngecek buat apakah num udah ada di seen tapi belum dimasukin ke hasil
        for num in nums2:
            if num in seen and num not in hasil:
                hasil.append(num)
        return hasil
        