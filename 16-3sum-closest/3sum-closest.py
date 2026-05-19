class Solution(object):
    def threeSumClosest(self, nums, target):
        #init close dulu buat pembanding
        nums.sort()
        close = nums[0] + nums[1] + nums[2]
        #for nya kayak 3 sum biasa
        for i in range(len(nums) - 2):
            # Early break: if i repeats, skip (optional, but can speed up)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #init left right kayak 3 sum
            left = i + 1
            right = len(nums) - 1

            while left < right:
                #itung jumlah buat pembanding utama
                cur = nums[i] + nums[left] + nums[right]
                
                #bandingin selisih target sama cur dan close kalo kecilan cur ya close ganti cur
                if abs(cur - target) < abs(close - target):
                    close = cur

                #kayak 2 pointer pada umumnya (while buat skipping duplicates for speed di three sum sebelum ada)
                if cur < target:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1      
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return close

