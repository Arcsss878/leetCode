class Solution(object):
    def maxArea(self, height):
        #pake two pointer sama siapin buat simpen terbesar
        left = 0
        right = len(height) - 1
        largest = 0

        #buat loop selama left != right
        while left < right:
            #cari luas (tinggi terpendek dikali sama selisih index buat luas)
            luas = min(height[right], height[left]) * (right-left)
            #kalo lebih besar luasnnya langsung di catet
            if luas > largest:
                largest = luas

            #gerakin pointer yang lebih kecil sapa tau lebih baik
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return largest
        

        #better solution(di ringkas aja sih, sama tambah while dalem if buat skip tinggi yang < atau = dengan yang udah di komputasiin)
        while left < right:
            luas = min(height[left], height[right]) * (right - left)
            largest = max(largest, luas)
    
            if height[left] < height[right]:
                # Skip all left heights that are <= current left height
                current_left = height[left]
                while left < right and height[left] <= current_left:
                    eft += 1
            else:
                # Skip all right heights that are <= current right height
                current_right = height[right]
                while left < right and height[right] <= current_right:
                     right -= 1