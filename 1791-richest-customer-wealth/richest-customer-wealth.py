class Solution(object):
    def maximumWealth(self, accounts):
        #buat penyimpan untuk maxnya
        max_wealth = 0
        #loop per customer
        # First iteration: customer = [1, 2, 3]
        # Second iteration: customer = [3, 2, 1]
        for customer in accounts:
            #jumlahin customer dalam 1 row itu
            c_sum = sum(customer)
            if c_sum > max_wealth:
                max_wealth = c_sum
        return max_wealth

        #other way
        return max(sum(customer) for customer in accounts)

        #note 
        rows = len(accounts)# number of customers
        cols = len(accounts[0])# number of banks per customer (assuming non-empty)
        