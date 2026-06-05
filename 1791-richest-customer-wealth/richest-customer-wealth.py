class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        for customer in accounts:
            c_sum = sum(customer)
            if c_sum > max_wealth:
                max_wealth = c_sum
        return max_wealth
        