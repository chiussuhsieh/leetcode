# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# 難度：Medium
# 類型：2D DP (Memoization)

# 思路：
# dfs(i, buying) = 從第 i 天開始，當前狀態是 buying 時的最大利潤
# buying=True：今天可以買股票
# buying=False：今天可以賣股票
# 每天有兩個選擇：
# 1. cooldown：什麼都不做，直接看明天（保持同樣的 buying 狀態）
# 2. 採取行動：
#    - 如果可以買：今天買進，扣掉 prices[i]，明天變成「能賣」狀態
#    - 如果可以賣：今天賣出，加上 prices[i]，因為要冷卻一天，跳到 i+2 變成「能買」狀態
# 用 dictionary 做 memoization，避免重複計算

# Time: O(n)，每個 (i, buying) 狀態只算一次
# Space: O(n)，memoization dictionary

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # key=(i, buying)，value=從第 i 天開始的最大利潤

        def dfs(i, buying):
            if i >= len(prices):
                return 0                    # 超出範圍，沒有更多利潤了

            if (i, buying) in dp:
                return dp[(i, buying)]      # 已經算過，直接回傳，避免重複計算

            cooldown = dfs(i + 1, buying)
            # 選擇1：今天不做任何事，明天繼續同樣的狀態

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                # 選擇2：今天買進，花掉 prices[i]
                # 明天狀態變成 not buying（可以賣了）
                dp[(i, buying)] = max(buy, cooldown)
                # 買或不買，取較大的利潤
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                # 選擇2：今天賣出，賺到 prices[i]
                # 要冷卻一天，所以跳到 i+2
                # 狀態變成 not buying（也就是 True，可以買了）
                dp[(i, buying)] = max(sell, cooldown)
                # 賣或不賣，取較大的利潤

            return dp[(i, buying)]

        return dfs(0, True)   # 從第 0 天開始，一開始處於「可以買」的狀態