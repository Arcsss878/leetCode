class Solution(object):
    def isValid(self, s):
        if len(s) % 2 is not 0:
            return False
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            else:
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
                else:
                    stack.append(s[i])
        if not stack:
            return True
        else :
            return False
