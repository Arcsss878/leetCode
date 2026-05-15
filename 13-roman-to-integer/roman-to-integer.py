class Solution(object):
    def romanToInt(self, s):
        rom_val = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        res = 0
        for i in range(len(s) - 1):
            if rom_val[s[i]] < rom_val[s[i+1]]:
                res -= rom_val[s[i]]
            else:
                res += rom_val[s[i]]
        
        res += rom_val[s[-1]]
        return res