class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        #inis dulu len biar gampang ini lainnya
        n = len(A)
        #frq ini cuman array yang 0 diulang sebanyak 0 + 1  buat place holder jum angka (0 ga dipake)
        freq = [0] * (n + 1)
        #buat penampung hasil sama countnya (ga perlu di reset biar nambah terus per ada yang baca)
        hasil = []
        common_count = 0
        #pake in range biar keluarnya index
        for i in range(n):
            # Process A[i]
            freq[A[i]] += 1
            #cek kalo freqnya udah 2 langsung tambah count
            if freq[A[i]] == 2:
                common_count += 1
            
            # Process B[i]
            freq[B[i]] += 1
            #cek kalo freqnya udah 2 langsung tambah count
            if freq[B[i]] == 2:
                common_count += 1
            
            #append jum count per loop tanpa di reset
            hasil.append(common_count)
        return hasil

            #freq = {}
            #ini tambahan aja buat contoh versi dict (sama ae sih cuman kalo lom di init di bikin dulu)
            # Process A[i]
            #if A[i] in freq:
            #    freq[A[i]] += 1
            #else:
            #    freq[A[i]] = 1
            #if freq[A[i]] == 2:
            #    common_count += 1
            
            # Process B[i]
            #if B[i] in freq:
            #    freq[B[i]] += 1
            #else:
            #    freq[B[i]] = 1
            #if freq[B[i]] == 2:
            #    common_count += 1