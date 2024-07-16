class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount 
        
        dp = [float('inf')] * (n + 1)
        
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, n + 1):
                dp[x] = min(dp[x - coin] + 1, dp[x])
                
                
        return dp[amount] if dp[amount] != float('inf') else -1
        
        
        