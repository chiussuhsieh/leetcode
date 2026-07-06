# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# 難度：Medium
# 類型：Array, Greedy
# 思路：
# 只要明天比今天貴，今天就買明天就賣
# iterate array，把所有上漲區間的差值累加進 totalProfit
# 不需要找最低最高點，貪心地抓住每一段上漲就是最大利潤
# Pattern 筆記：
# 這題的 pattern 是「貪心法，累加所有上漲區間」
# 只要 prices[i+1] > prices[i] 就加進 totalProfit
# 下次看到「可以無限次買賣股票求最大利潤」就用這個方法
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        for i in range(len(prices)-1):       # 到倒數第二個，避免 out of bounds
            if prices[i+1] > prices[i]:
                profit = prices[i+1] - prices[i]  # 計算上漲區間的差值
                totalProfit += profit
            else:
                continue
        return totalProfit