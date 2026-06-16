class Solution(object):
    def processStr(self, s):
        hasil = ""
        for i in s:
            if i == '#':
                hasil += hasil
            elif i == '%':
                hasil = ''.join(reversed(hasil))
            elif i == '*':
                hasil = hasil[:-1]
            else:
                hasil += i
        return hasil

        