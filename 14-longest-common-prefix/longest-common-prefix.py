class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for s in strs[1:]:
            # Reduce prefix until it matches the start of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # chop off last character
                if not prefix:
                    return ""
        return prefix
        