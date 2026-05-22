class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
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
            

        