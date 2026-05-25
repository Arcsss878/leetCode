class Solution(object):
    def canReach(self, s, minJump, maxJump):
        n = len(s)
        if s[-1] != '0':
            return False
        
        dp = [False] * n
        dp[0] = True
        # prefix sum of reachable counts
        prefix = [0] * n
        prefix[0] = 1  # dp[0] is reachable
        
        for i in range(1, n):
            if s[i] == '0':
                # compute left and right bounds of window
                left = max(0, i - maxJump)
                right = i - minJump
                if right >= 0:
                    # number of reachable positions in window
                    reachable_count = prefix[right] - (prefix[left-1] if left > 0 else 0)
                    if reachable_count > 0:
                        dp[i] = True
            # update prefix sum
            prefix[i] = prefix[i-1] + (1 if dp[i] else 0)
        
        return dp[-1]