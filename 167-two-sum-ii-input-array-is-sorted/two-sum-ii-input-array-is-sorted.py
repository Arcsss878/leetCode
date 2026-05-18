class Solution(object):
    def twoSum(self, numbers, target):
        #buat pointer buat penanda ujung kanan kiri
        left = 0
        right = len(numbers) - 1
        #selama kiri belum melewati kanan lanjut
        while left < right:
            #jumlah angka ujung kanan sama kiri
            cur_sum = numbers[left] + numbers[right]
            #kalo sama langsung selesai
            if cur_sum == target:
                return [left + 1, right + 1]
            #kalo kurang dari target berarti angka kirinya kurang besar jadi kita geser
            elif cur_sum < target:
                left += 1
            #ini logicnya sama kayak kurang dari cuman kebalikan karena cari yang besar
            else:
                right -= 1
