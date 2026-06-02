# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/
# 難度：Medium
# 類型：Intervals, Greedy

# 思路：
# 最少移除 = 最多保留不重疊的 intervals
# 先按起點排序，遇到重疊時，保留 end 較小的 interval
# 因為 end 較小的留著，跟後面重疊的機率較小
# 每次重疊就 count += 1，代表移除一個

# Time: O(n log n)，排序
# Space: O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])  # 按起點從小到大排序
        count = 0                            # 記錄移除的數量
        prevEnd = intervals[0][1]            # 記錄前一個 interval 的 end

        for interval in intervals[1:]:       # 從第二個開始，第一個已經放進 prevEnd
            if interval[0] < prevEnd:        # 當前 interval 的起點 < 前一個的終點，重疊！
                count += 1                   # 移除一個
                prevEnd = min(interval[1], prevEnd)
                                             # 保留 end 較小的，跟後面重疊的機率較小
            else:                            # 不重疊
                prevEnd = interval[1]        # 更新 prevEnd 為當前 interval 的 end

        return count                         # 最少需要移除幾個 interval