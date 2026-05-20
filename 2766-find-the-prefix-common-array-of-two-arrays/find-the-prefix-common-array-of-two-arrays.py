class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        freq = [0] * (n + 1)
        hasil = []
        common_count = 0
        for i in range(n):
            # Process A[i]
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common_count += 1
            
            # Process B[i]
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common_count += 1
            
            hasil.append(common_count)
        return hasil