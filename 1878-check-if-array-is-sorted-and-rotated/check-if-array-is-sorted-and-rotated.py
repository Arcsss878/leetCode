class Solution(object):
    def check(self, nums):
        # Di array yang sudah urut terus kena rotated, pasti ada setidaknya satu tempat 
        # dimana angka kiri lebih besar dari angka kanan (kita sebut "drop").
        # Kalau array urut tanpa rotasi, drop nya ada 0 (tetap true karena rotasi 0 diperbolehkan).
        # Kalau array urut dirotasi, akan ada tepat 1 drop di titik rotasi.

        # Pertama, cek wrap-around: angka terakhir > angka pertama?
        # Karena dalam array terurut yang dirotasi, elemen terakhir seharusnya <= elemen pertama.
        # Jika lebih besar, itu berarti ada drop di sambungan lingkaran.
        if nums[-1] > nums[0]:
            count = 1
        else:
            count = 0
        
        # Lalu cek semua pasangan berurutan di dalam array (dari index 0 sampai n-2)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                count += 1
            if count > 1:
                return False
        return True

        n = len(nums)
        drops = 0
        # Loop dari i = 0 sampai n-1 (semua elemen)
        for i in range(n):
            # Bandingkan nums[i] dengan nums[(i+1) % n]
            # (i+1) % n membuat indeks kembali ke 0 setelah elemen terakhir, jadi kita memeriksa pasangan melingkar (wrap-around)
            if nums[i] > nums[(i+1) % n]:
                drops += 1
            # Jika sudah lebih dari 1 drop, langsung return False
            if drops > 1:
                return False
        return True

    # Pendekatan ini lebih sederhana karena:
    # 1. Tidak perlu mengecek wrap terpisah (nums[-1] > nums[0]).
    # 2. Menggunakan modulo untuk membuat array melingkar: indeks (i+1) % n memastikan bahwa setelah elemen terakhir,
    #    kita kembali ke elemen pertama (lingkaran tertutup).
    # 3. Dalam array yang merupakan hasil rotasi dari array terurut (non‑decreasing), akan ada paling banyak satu
    #    tempat di mana suatu elemen lebih besar dari elemen berikutnya (dalam urutan melingkar).
    # 4. Jika drops <= 1, maka array valid; jika drops > 1, array tidak valid.
        