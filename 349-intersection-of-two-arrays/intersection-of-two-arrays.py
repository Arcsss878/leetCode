class Solution(object):
    def intersection(self, nums1, nums2):
        seen = {}
        hasil = []
        for num in nums1:
            seen[num] = True
        for num in nums2:
            if num in seen and num not in hasil:
                hasil.append(num)
        return hasil
        