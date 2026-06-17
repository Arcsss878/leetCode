class Solution(object):
    def intToRoman(self, num):
        # Daftar lengkap nilai dan simbol Romawi (dari besar ke kecil, termasuk angka spesialnya juga)
        #udah urut ini value sama simbolnya 
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        result = ""
        #for loop sepanjang valuenya
        for i in range(len(values)):
            #selama num lebih dari sama dengan val loop terus
            while num >= values[i]:
                #result tambah simbolnya sekatang terus kurangi num sama valuenya, cek kalo masih lebih dari value brt loop lagi
                result += symbols[i]
                num -= values[i]
        return result

        #other way
        # Arrays for each place value (index 0 to 9)
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] #1-9
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] #10-90
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] #100-900
        thousands = ["", "M", "MM", "MMM"] #1000 - 1000000

        # langsung ambil per digitnya jadi misal 1994
        return (
            thousands[num // 1000] + #index 1, M
            hundreds[(num % 1000) // 100] + #index 1, CM
            tens[(num % 100) // 10] + #index 9, XC
            ones[num % 10] #index 4, IV
        )
        