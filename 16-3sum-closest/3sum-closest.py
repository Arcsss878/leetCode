class Solution(object):
    def threeSumClosest(self, nums, target):
        #init close dulu buat pembanding
        nums.sort()
        close = nums[0] + nums[1] + nums[2]
        #for nya kayak 3 sum biasa
        for i in range(len(nums) - 2):
            # Early break: if the smallest possible sum with this i is already > target
            # and its difference is >= current best difference, then no need to try larger i
            # because sums will only increase.
            min_sum = nums[i] + nums[i+1] + nums[i+2]
            if min_sum > target:
                # If even the minimum sum is above target, check if it's closer
                if abs(min_sum - target) < abs(close - target):
                    close = min_sum
                # Since any other i will give even larger sums (array sorted), we can break
                break
            
            # Optional: if max possible sum with this i is < target, 
            # we might still need to check larger i, so no break.
            # But we can update closest if this max sum is closer.
            max_sum = nums[i] + nums[-2] + nums[-1]
            if max_sum < target:
                if abs(max_sum - target) < abs(close - target):
                    close = max_sum
                continue  # try next i, because larger i might get closer from below

            #gapake yang diatas ini udah jalan tapi kalo pake jadi kenceng run time e

            #init left right kayak 3 sum
            left = i + 1
            right = len(nums) - 1

            while left < right:
                #itung jumlah buat pembanding utama
                cur = nums[i] + nums[left] + nums[right]
                
                #bandingin selisih target sama cur dan close kalo kecilan cur ya close ganti cur
                if abs(cur - target) < abs(close - target):
                    close = cur

                #kayak 2 pointer pada umumnya
                if cur < target:
                    left += 1   
                else:
                    right -= 1
        return close

