# 252. Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/
# 難度：Easy
# 類型：Intervals

# 思路：
# 能參加所有會議 = 所有 intervals 不重疊
# 先按起點排序，然後從左到右掃
# 如果當前 interval 的起點 < 前一個的終點，代表重疊，return False
# 全部掃完沒有重疊，return True

# Time: O(n log n)，排序
# Space: O(1)

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True                     # 沒有會議，直接 True

        intervals.sort(key=lambda i: i[0]) # 按起點從小到大排序
        prevEnd = intervals[0][1]          # 記錄前一個會議的結束時間

        for interval in intervals[1:]:     # 從第二個開始
            if interval[0] < prevEnd:      # 當前會議的起點 < 前一個的終點，重疊！
                return False               # 時間衝突，無法參加所有會議
            else:
                prevEnd = interval[1]      # 不重疊，更新 prevEnd

        return True                        # 全部掃完沒有重疊，可以參加所有會議