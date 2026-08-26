class Solution:
    def climbStairs(self, n: int) -> int:

        memo = [-1]*n

        def dp(i):
            if i >= n:
                return i==n
            if memo[i]!= -1: 
                return memo[i]
            memo[i] = dp(i+1) + dp(i+2)
            return memo[i]
        

        return dp(0)

        
        

        