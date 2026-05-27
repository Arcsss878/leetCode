class Solution(object):
    def numberOfSpecialChars(self, word):
        # Array untuk indeks terakhir kemunculan huruf kecil (a-z)
        # Diisi -1 artinya belum ada
        last_lower = [-1] * 26
        # Array untuk indeks pertama kemunculan huruf besar (A-Z)
        # Diisi dengan tak terhingga (inf) artinya belum ada
        first_upper = [float('inf')] * 26
        
        for i, ch in enumerate(word):
            #kalo valuenya lower case
            if ch.islower():
                #idx ini buat menentukan di index mana ch ini
                idx = ord(ch) - ord('a')
                # Simpan indeks terakhir (terus diupdate)
                last_lower[idx] = i
            else:  # huruf besar
                idx = ord(ch) - ord('A')
                # Catat indeks pertama (hanya jika belum pernah)
                if first_upper[idx] == float('inf'):
                    first_upper[idx] = i
        
        count = 0
        for i in range(26):
            # Jika kedua bentuk ada
            if last_lower[i] != -1 and first_upper[i] != float('inf'):
                # Syarat: semua huruf kecil harus sebelum huruf besar pertama
                # Cukup periksa indeks terakhir huruf kecil < indeks pertama huruf besar
                if last_lower[i] < first_upper[i]:
                    count += 1
        return count