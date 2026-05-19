class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        close = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                
                if abs(cur - target) < abs(close - target):
                    close = cur

                if cur > target:
                    right -= 1      
                else:
                    left += 1
        return close

