# 518. Coin Change II
# https://leetcode.com/problems/coin-change-ii/
# 難度：Medium
# 類型：1D DP

# 思路：
# dp[i] = 湊出金額 i 有幾種不同的組合方式
# 跟 Coin Change 不同：這題的硬幣使用順序不重要（[1,2] 跟 [2,1] 算同一種）
# 解決方法：把 coin 放在外層 loop，確保每種硬幣是依序處理
# 這樣可以避免同一組硬幣因為使用順序不同而被重複計算
# base case：dp[0] = 1，湊出金額 0 只有一種方法：什麼都不選

# Time: O(amount * len(coins))
# Space: O(amount)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)   # dp[i] = 湊出金額 i 的方法數
        dp[0] = 1                  # base case：什麼都不選，一種方法

        for coin in coins:                      # 固定一種硬幣，依序處理每種硬幣
            for i in range(coin, amount + 1):    # 從這個硬幣的面額開始（避免負數 index）
                dp[i] += dp[i - coin]
                # 用這個硬幣湊出 i，方法數 = 湊出 (i - coin) 的方法數
                # 累加進 dp[i]，代表「之前累積的方法 + 這個硬幣帶來的新方法」

        return dp[amount]   # 湊出目標金額的所有組合方式總數