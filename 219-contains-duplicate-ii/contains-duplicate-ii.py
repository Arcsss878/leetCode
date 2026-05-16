class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        # ni isine angka yang uda diliat sama index e dimana
        seen = {}
        # pake enumerate karena butuh sama indexnya juga
        for i, num in enumerate(nums):
            # ngecek kalo num ada di seen dan index num sekarang - index num sebelum <= k
            # bakal return true karena syarat true itu kalo duplikatnya setidaknya sejauh k
            if num in seen and i - seen[num] <= k:
                return True
            #ini cuman memperbaharui index num trakhir diliat
            seen[num] = i
        return False