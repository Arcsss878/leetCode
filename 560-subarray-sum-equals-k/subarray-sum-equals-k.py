class Solution(object):
    def subarraySum(self, nums, k):
        freq = {}
        freq[0] = 1
        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num
            target = current_sum - k
            count += freq.get(target, 0)
            freq[current_sum] = freq.get(current_sum, 0) + 1
        return count
