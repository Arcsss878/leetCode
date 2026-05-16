class Solution(object):
    def isAnagram(self, s, t):
        #pakai sorted(), nanti dirapiin terus di bandingin
        #return sorted(s) == sorted(t)

        #pake Counter()
        #return Counter(s) == Counter(t)

        #cara lebih efektif
        #langsung salah klo panjang beda
        if len(s) != len(t): 
            return False
        count = {}
        for char in s: #char ni nanti mbaca karakter 1 1
            #get():cek dict ada isi ?kalo ga ada get defnya 0
            count[char] = count.get(char,0) + 1                  
        for char in t:
            #langsung salah kalo ga ada
            if char not in count: 
                return False
            #kurangi 1 1 sampe habis kalo emang anagam
            count[char] -= 1 
            #kalo negatif, t punya lebih banyak char dari s(misal abb, aab nanti b bakal mines)
            if count[char] < 0:
                return False 
        return True

        #fastest
        # REASONING: This solution uses an array of size 26 instead of a dictionary.
        # It's faster (O(1) space) but ONLY works for lowercase English letters.
        # Each index represents a letter: 0='a', 1='b', 2='c', ..., 25='z'
        
        # First check: different lengths mean they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Create array of 26 zeros (one for each lowercase letter)
        # Space complexity: O(1) because array size is fixed (26)
        #count = [0] * 26
        
        # REASONING: First pass - count frequency of each letter in string s
        # For each character, convert it to an index and increment
        # Example: s = "aab" → count[0]=2 (for 'a'), count[1]=1 (for 'b')
        for char in s:
            # ord() gives ASCII value: ord('a')=97, ord('b')=98, etc.
            # Subtract ord('a') to get 0-based index
            index = ord(char) - ord('a')
            count[index] += 1
        
        # REASONING: Second pass - subtract frequencies using string t
        # If t is an anagram, all counts should return to zero
        for char in t:
            index = ord(char) - ord('a')
            count[index] -= 1
            
            # REASONING: If count becomes negative, t has MORE of this letter than s
            # Example: s="aab"(a:2,b:1) vs t="abb"(a:1,b:2)
            # When processing second 'b' in t, count[1] goes 1→0→(-1) → ANGRAM FAILS
            if count[index] < 0:
                return False
        
        # REASONING: Check if all counts are zero
        # all() returns True only if every element in the list is zero
        # This means s and t had exactly the same character frequencies
        # Example: s="ab", t="ba" → count becomes [0,0,0...] → all zero → True
        return all(c == 0 for c in count)
        
        # ALTERNATIVE: We could return True here without the all() check
        # Because if any count wasn't zero, the previous loop would have
        # created a negative number (t has more) OR we'd have leftover positives
        # But the all() check is safer and handles edge cases

