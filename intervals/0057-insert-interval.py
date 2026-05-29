# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/
# 難度：Medium
# 類型：Intervals

# 思路：
# 對每個 interval 判斷跟 newInterval 的關係：
# 1. newInterval 在左邊（不重疊）：把 newInterval 和後面所有 interval 直接加入結果
# 2. newInterval 在右邊（不重疊）：當前 interval 直接加入結果，繼續往右找
# 3. 重疊：merge！取兩個 interval 的 min start 和 max end
# 注意：newInterval 可能跟多個 interval 重疊，所以要一直 merge 直到不重疊為止

# Time: O(n)
# Space: O(n)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [] # 記錄結果
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # newInterval 的終點 < 當前 interval 的起點 # newInterval 完全在左邊，不重疊
                res.append(newInterval)  # 把 newInterval 加入結果
                return res + intervals[i:] # 後面的 interval 都不需要處理，直接接上去
            elif newInterval[0] > intervals[i][1]: # newInterval 的起點 > 當前 interval 的終點 # newInterval 完全在右邊，不重疊
                res.append(intervals[i]) # 當前 interval 直接加入結果，繼續往右找

            else:
                newInterval = (min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1]))
            res.append(newInterval) # 重疊！merge 兩個 interval # 取兩個 interval 的 min # 不馬上加入結果，因為後面可能還有重疊的 interval start 和 max end
                 # loop 結束，newInterval 還沒加入結果
            
                
        return res
            
