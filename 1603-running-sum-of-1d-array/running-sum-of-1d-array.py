class Solution(object):
    def runningSum(self, nums):
        #buat penyimpan hasil dan akumulasi angka
        curr_sum = 0
        r = []
        #tambah sum tiap putaran dan tambah di array
        for i in nums:
            curr_sum += i
            r.append(curr_sum)
        return r
        