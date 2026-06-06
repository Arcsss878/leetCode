class Solution(object):
    def isIsomorphic(self, s, t):
        #kalau panjangnya beda langsung salah
        if len(s) != len(t):
            return false
        #buat mapping masing"(untuk mengetahui masing masing huruf menggantikan apa)
        mapSt = {}
        mapTs = {}
        #loop sebanyak huruf s/t
        for i in range(len(s)):
            #buat penyimpanan(biar lbh gampang di reuse)
            c1 = s[i]
            c2 = t[i]

            # Check forward mapping, kalo hurufnya udah ada di mapnya dan isinya ga sama kayak c2 berarti salah
            if c1 in mapSt and mapSt[c1] != c2:
                return False
            # Check backward mapping, aturan diatas berlaku buat backwarnya juga
            if c2 in mapTs and mapTs[c2] != c1:
                return False

            # Establish mappings
            mapSt[c1] = c2
            mapTs[c2] = c1
        return True
        