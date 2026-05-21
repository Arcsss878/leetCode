class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        #jawaban optimal kata gpt saya       
        # Step 1: store all prefixes of arr1 in a set
        prefixes = set()
        for num in arr1:
            s = str(num)
            for i in range(1, len(s)+1):   # i = length of prefix
                prefixes.add(s[:i])
        
        # Step 2: check each number in arr2
        max_len = 0
        for num in arr2:
            s = str(num)
            for i in range(1, len(s)+1):
                if s[:i] in prefixes:
                    max_len = max(max_len, i)
        return max_len

        #kena time limit lho ya rek pake brute force(btw ni ga sah pake if else panjang arr soale ga ngaruh)
        #hasil = 0
        #for a in arr1:
        #    compA = str(a)
        #    for b in arr2:
        #        compB = str(b)
                # Find common prefix length of sa and sb
        #        counter = 0
        #        limit = min(len(compA), len(compB))
        #        for i in range(limit):
        #            if compA[i] == compB[i]:
        #                counter += 1
        #            else:
        #                break
        #        if counter > hasil:
        #            hasil = counter
        #return hasil
