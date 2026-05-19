class Solution(object):
    def maxArea(self, height):
        #pake two pointer sama siapin buat simpen terbesar
        left = 0
        right = len(height) - 1
        largest = 0

        while left < right:
            luas = min(height[right], height[left]) * (right-left)
            if luas > largest:
                largest = luas

            if height[right] < height[left]:
                right -=1
            else:
                left +=1
        return largest
        