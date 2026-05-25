class Solution(object):
    def canReach(self, s, minJump, maxJump):
        n = len(s)
        # Jika karakter terakhir bukan '0', tidak mungkin mencapai akhir
        if s[-1] != '0':
            return False
        
        # dp[i] = apakah index i dapat dicapai (mulai dari 0)
        dp = [False] * n
        dp[0] = True  # posisi awal selalu dapat dicapai
        
        # prefix[i] = jumlah index 0..i yang dp-nya True (reachable)
        prefix = [0] * n
        prefix[0] = 1  # index 0 reachable
        
        for i in range(1, n):
            # Kita hanya perlu memeriksa jika s[i] == '0'
            if s[i] == '0':
                # Batas kiri dan kanan dari window (index-index sebelumnya yang bisa melompat ke i)
                left = max(0, i - maxJump)      # j minimal yang bisa loncat ke i
                right = i - minJump             # j maksimal yang bisa loncat ke i
                
                # Jika right >= 0, artinya masih ada j yang mungkin
                if right >= 0:
                    # Hitung berapa banyak reachable index dalam [left, right]
                    # Jika left > 0, count = prefix[right] - prefix[left-1]
                    # Jika left == 0, count = prefix[right] (karena prefix[-1] tidak terdefinisi)
                    reachable_count = prefix[right] - (prefix[left-1] if left > 0 else 0)
                    
                    # Jika ada setidaknya satu reachable index dalam window, i bisa dicapai
                    if reachable_count > 0:
                        dp[i] = True
            
            # Update prefix sum: prefix[i] = prefix[i-1] + (1 jika dp[i] True)
            prefix[i] = prefix[i-1] + (1 if dp[i] else 0)
        
        # Apakah index terakhir dapat dicapai?
        return dp[-1]