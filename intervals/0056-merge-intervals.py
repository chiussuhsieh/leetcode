# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# 難度：Medium
# 類型：Intervals

# 思路：
# 先按起點排序，確保從左到右掃，當前 interval 的 start 一定 >= 前一個的 start
# 排序後只剩兩種情況：重疊或不重疊
# 重疊：更新 res 最後一個的 end = max(當前 end, 前一個 end)
# 不重疊：直接加入 res
# 只需要跟 res[-1] 比較，因為已經排序，不可能跟更前面的重疊

# Time: O(n log n)，排序
# Space: O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])  # 按起點從小到大排序
        res = []
        res.append(intervals[0])             # 先把第一個放進去當基準

        for interval in intervals:           # 從左到右掃每個 interval
            if interval[0] <= res[-1][1]:   # 當前 interval 的起點 <= res 最後一個的終點
                                            # 重疊！
                res[-1][1] = max(interval[1], res[-1][1])
                                            # 只需要更新 end，取兩者較大的
                                            # start 不需要更新，排序保證前一個 start 一定較小
            else:
                res.append(interval)        # 不重疊，直接加入 res

        return res