class Solution(object):
    def isValid(self, s):
        #better code (lebih ringkas ga banyak ulang ulang)
        #ini buat mapping yang tinggal di cocok cocokin
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            #cek inputannya ini parentheses atau bukan
            if ch in mapping: # ch ni nanti closing bracketnya
                #kalo stak kosong atau top of stack ga sama kayak yang ada di mapping
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else:
                # opening bracket
                stack.append(ch)
        return not stack  # True if stack is empty
        
        #ini buatan dair nol jadi alakadarnya
        #ngecek kalo ganjil langsung false
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in range(len(s)):
            #kalo stack lom ada tambah dulu
            if not stack:
                stack.append(s[i])
            else:
                #buatin checking per parentheses, kalo sama kayak top of stack langsung pop
                if s[i] ==  ")":
                    if "(" == stack[-1]:
                        stack.pop()
                    else:
                        return False
                elif s[i] ==  "}":
                    if "{" == stack[-1]:
                        stack.pop()
                    else:
                        return False
                elif s[i] == "]":
                    if "[" == stack[-1]:
                        stack.pop()
                    else:
                        return False
                #ini perlu buat kalo dia parentheses berlapis, jadi nambah lagi kalo kurung buka
                else:
                    stack.append(s[i])
        #last cek buat kalo stack masih ada kurung yang belum ketutup
        if not stack:
            return True
        else :
            return False
