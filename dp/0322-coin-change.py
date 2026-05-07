# 322. Coin Change
# https://leetcode.com/problems/coin-change/
# 難度：Medium
# 類型：DP

# 思路：
# dp[i] = 湊出金額 i 最少需要幾枚硬幣
# 對每個金額 i，試所有硬幣，取最小枚數
# dp[i] = min(dp[i], dp[i-coin]+1) for each coin

# 注意：初始化用 float('inf') 而非 0
# 因為 min() 會讓 0 永遠贏，導致答案全部是 0

# Time: O(amount * len(coins)), Space: O(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        # dp[0] = 0：湊出 0 元需要 0 枚
        # 其餘設成 inf：代表還不知道，讓任何真實答案都能覆蓋它
        for i in range(1, amount+1):
            # 從金額 1 開始，逐步建到 amount
            # dp[0] 已經確定，不需要從 0 開始
            for coin in coins:
                # 對每個金額 i，試所有硬幣
                if i - coin >= 0:
                    # 確保不會 index 超出範圍
                    # 例如 i=2, coin=4 → 2-4=-2，這枚硬幣用不了
                    dp[i] = min(dp[i], dp[i-coin]+1)
                    # dp[i-coin]：湊出「目標金額 - 這枚硬幣」的最少枚數
                    # +1：再加上這枚硬幣
                    # min：跟目前最優解比較，保留較小的
        return dp[amount] if dp[amount] != float('inf') else -1
    # dp[amount] 就是湊出目標金額的最少枚數
        # 如果還是 inf，代表湊不出來，回傳 -1