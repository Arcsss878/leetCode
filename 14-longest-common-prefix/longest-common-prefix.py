class Solution(object):
    def longestCommonPrefix(self, strs):
        #cek kalo listnya kosong
        if not strs:
            return ""
        # Start with the first string as the prefix
        prefix = strs[0]
        for s in strs[1:]:
            # Reduce prefix until it matches the start of s
            #s.startswith(prefix) is a built-in string method that returns True if string s starts with the characters in prefix
            #jadi ni selama s ga start sama character di prefix bakal kena loop misal "flow" start with "flower" kan enggak sampek kita pretelin blakangnya prefix 1 1
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # chop off last character
                #kalo prefix dipretelin sampe kosong berarti ya ga ada jadi return
                if not prefix:
                    return ""
        return prefix
        