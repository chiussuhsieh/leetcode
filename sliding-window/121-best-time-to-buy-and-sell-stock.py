# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 難度: Easy
# Type: Sliding Window (單指針遍歷)

# 思路:
# 用一個指針 right 從左到右掃過整個陣列,同時維護一個 minPrice 變數
# 代表「目前為止看過的最低價格」。
# 每走到一天,先計算「如果今天賣出」可以獲得的獲利(今天價格 - 目前最低價),
# 並且更新 maxProfit。
# 接著再檢查今天的價格是否比目前的 minPrice 還低,如果是就更新 minPrice。
# 這個順序很重要:一定要先算獲利、再更新 minPrice,
# 因為不能在同一天內「先買後賣」,所以獲利要用「更新前」的 minPrice 來算。
# 這樣只需要一次遍歷,就能同時追蹤「最低買入點」和「最大獲利」。

# Pattern 筆記:
# 這題的 pattern 是「單指針遍歷 + 維護目前為止的最佳值」,
# 下次看到「找一個區間內,左邊最小、右邊最大」的題目,
# 且只需要遍歷一次就能同步更新兩個追蹤值時,就可以用這個方法。

# Time complexity: O(n),只遍歷一次陣列
# Space complexity: O(1),只用了兩個額外變數

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = 0  # 指針從第 0 天開始
        minPrice = prices[0]  # 初始化最低價為第一天的價格
        maxProfit = 0  # 初始化最大獲利為 0(還沒開始交易)

        while right < len(prices):  # 走訪每一天的價格
            profit = prices[right] - minPrice  # 計算如果今天賣出的獲利
            maxProfit = max(maxProfit, profit)  # 更新目前為止的最大獲利

            if prices[right] < minPrice:  # 如果今天價格比目前最低價還低
                minPrice = prices[right]  # 更新最低價

            right += 1  # 指針往右移動一天

        return maxProfit  # 回傳最大獲利