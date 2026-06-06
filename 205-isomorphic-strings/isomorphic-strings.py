class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return false
        mapSt = {}
        mapTs = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            # Check forward mapping
            if c1 in mapSt and mapSt[c1] != c2:
                return False
            # Check backward mapping
            if c2 in mapTs and mapTs[c2] != c1:
                return False

            # Establish mappings
            mapSt[c1] = c2
            mapTs[c2] = c1
        return True
        