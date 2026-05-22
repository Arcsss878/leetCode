class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            #cari mid dulu buat nyari posisi target dimana
            mid = (left + right) // 2
            #kalo mid sama langsug kembaliin
            if nums[mid] == target:
                return mid
            
            #jadi ni intine ngecek kalo di kanan apa kiri yang lebih besar dari mid
            #kalo di kanan coba liat apakah target diantara mid sama left, kalo ga ya brt target dikanan dan sebaliknya
            #ini nanti kalo udah ketemu posisi rght/left digeser jadi mid -/+1 jadi memperkecil array pencariannya
            # Check which half is sorted
            if nums[left] <= nums[mid]:   # left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1      # target in left sorted half
                else:
                    left = mid + 1       # target in right half
            else:                         # right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1       # target in right sorted half
                else:
                    right = mid - 1      # target in left half
        return -1
            

        