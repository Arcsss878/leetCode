class Solution(object):
    def subarraySum(self, nums, k):
        # freq stores how many times a certain prefix sum has appeared so far
        # prefix sum = sum of elements from index 0 to current index
        freq = {}
        
        # Initialization: prefix sum 0 appears once (before we start)
        # This handles subarrays that start at index 0
        freq[0] = 1
        
        current_sum = 0  # running prefix sum
        count = 0        # total number of subarrays that sum to k
        
        for num in nums:
            # add current number to running sum
            current_sum += num
            
            # We want subarrays ending at current index that sum to k.
            # If current_sum - previous_prefix = k,
            # then previous_prefix = current_sum - k.
            target = current_sum - k
            
            # How many times have we seen a prefix sum equal to target?
            # Each such occurrence means a subarray that sums to k
            # ends at current index.
            count += freq.get(target, 0)
            
            # Record the current prefix sum for future indices
            # (how many times it has occurred)
            freq[current_sum] = freq.get(current_sum, 0) + 1
        
        return count