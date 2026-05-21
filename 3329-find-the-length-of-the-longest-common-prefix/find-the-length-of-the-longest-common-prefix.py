class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        #jawaban optimal kata gpt saya       
        # Step 1: store all prefixes of arr1 in a set
        #ini buat empty set (ntar yang kesimpen disini gamungkin dobel dobel angkanya)
        prefixes = set()
        for num in arr1:
            s = str(num)
            #i represents the length of the prefix we want to extract, from 1 up to the full length of the string.
            #range(1, len(s)+1) gives i = 1, 2, ..., len(s).
            for i in range(1, len(s)+1):   # i = length of prefix
                #s[:i] takes the first i characters of the string (the prefix of length i).
                #Add that prefix to the prefixes set.
                #Example: For num = 123, we add "1", "12", "123".
                prefixes.add(s[:i])
        
        # Step 2: check each number in arr2
        max_len = 0
        for num in arr2:
            s = str(num)
            #loop dari awal sampek akhir s
            for i in range(1, len(s)+1):
                #note : i ngecek panjang prefix yang di cek ya, jadi ini cek apakah prefix dengan panjang i ada
                if s[:i] in prefixes:
                    #kalo ada ganti max len sama value terbesar antara i dan max len
                    max_len = max(max_len, i)
        #kelar terus balikin
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
