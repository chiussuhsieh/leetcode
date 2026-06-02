# 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/
# 難度：Medium
# 類型：Intervals, Heap

# 思路：
# 最少需要幾間會議室 = 同時重疊的最多會議數量
# 先按起點排序，用 min heap 追蹤每間會議室的結束時間
# heap[0] 永遠是最早結束的會議室
# 如果最早結束的會議室已經空了（heap[0] <= 當前起點），重複使用
# 否則新開一間會議室
# 不管有沒有空房，都要把當前會議的結束時間加進 heap
# 最後 heap 的大小就是需要的會議室數量

# Time: O(n log n)，排序 + heap 操作
# Space: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        intervals.sort(key=lambda i: i[0])  # 按起點從小到大排序
        heap = []                            # min heap，記錄每間會議室的結束時間

        for interval in intervals:           # 從左到右掃每個會議
            if heap and heap[0] <= interval[0]:
                # heap 不是空的，且最早結束的會議室已經空了
                heapq.heappop(heap)          # 空出這間會議室（移除舊的結束時間）

            heapq.heappush(heap, interval[1])
            # 不管有沒有空房，都要分配一間給當前會議
            # 有空房：重複使用（pop 舊的，push 新的）
            # 沒空房：新開一間（直接 push）

        return len(heap)                     # heap 大小 = 同時使用中的會議室數量