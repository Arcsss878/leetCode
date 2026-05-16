class Solution(object):
    def isAnagram(self, s, t):
        #pakai sorted(), nanti dirapiin terus di bandingin
        #return sorted(s) == sorted(t)

        #cara lebih efektif
        if len(s) != len(t): #langsung salah klo panjang beda
            return False
        count = {}
        for char in s: #char ni nanti mbaca karakter 1 1
            #get():cek dict ada isi ?kalo ga ada get defnya 0
            count[char] = count.get(char,0) + 1                  
        for char in t:
            if char not in count: #langsung salah kalo ga ada
                return False
            count[char] -= 1 #kurangi 1 1 sampe habis kalo emang anagam
            if count[char] < 0:
                return False #kalo negatif, t punya lebih banyak char dari s
        return True