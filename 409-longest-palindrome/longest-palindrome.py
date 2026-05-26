class Solution(object):
    def longestPalindrome(self, s):
        #ini pake counter langsung jadi biar langsung dibikinin dictionary
        #simpen total buat hasil sama ganjil buat nyimpen angka
        letter = Counter(s)
        total = 0
        ganjil = False
        #ini ngecek value per hurufnya di kasik nama count
        for count in letter.values():
            #kalo genap langsung tambah aja
            if count % 2 == 0:
                total += count
            #kalo ganjil simpen angka ganjilnya 1(ga bisa lebih), kalo ganjilnya cuman 1 huruf langsung ga dianggep soalnya kena -1
            else:
                ganjil = True
                total += count - 1
        #cek apakah ada ganjil yang kesimpen, kalo ya tambah dulu 1 kalo ga langsung return
        if ganjil:
            return total + 1
        return total
        
        #code lebih pendek:
        freq = Counter(s)
        length = 0
        odd_exists = False
        for v in freq.values():
            #kalo ganjil nanti pasti kena mines 1 disini
            length += v - (v % 2)   # v if even, v-1 if odd
            #kalo hasilnya 1(true, ganjil) langsung eksekusi makanya oddnya kecatet, kalo genap hasilnya 0 jadi false dan ga jalan
            if v % 2:
                odd_exists = True
        return length + (1 if odd_exists else 0)