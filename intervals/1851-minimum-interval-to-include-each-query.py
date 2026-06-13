# 1851. Minimum Interval to Include Each Query
# https://leetcode.com/problems/minimum-interval-to-include-each-query/
# 難度：Hard
# 類型：Intervals, Heap

# 思路：
# 對每個 query，找包含它的最小 interval
# 關鍵：把 queries 排序，用 pointer i 從左到右加 interval，不需要回頭
# 用 min heap 按 interval 大小排序，heap[0] 永遠是最小的
# heap 存 (size, end)：size 用來排序，end 用來判斷是否包含 query
# 每個 query 處理完後存進 dictionary，最後按原始順序取出答案

# Time: O(n log n + q log q)，排序 + heap 操作
# Space: O(n + q)

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()        # 按起點排序（預設按第一個元素）
        minHeap = []            # min heap，存 (size, end)，按 size 排序
        res = {}                # dictionary，記錄每個 query 對應的答案
        i = 0                   # intervals 的 pointer，記錄加到哪裡了

        for q in sorted(queries):               # 按 query 值從小到大處理
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                # 把所有 start <= q 的 interval 加進 heap
                # (size, end)：size 用來找最小，end 用來判斷是否包含 query
                i += 1                          # pointer 往前，下個 query 從這裡繼續

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
                # 移除 end < q 的 interval
                # 這些 interval 不包含當前 query，不需要了

            res[q] = minHeap[0][0] if minHeap else -1
            # heap[0][0] 是最小 interval 的大小
            # heap 是空的代表沒有包含 q 的 interval，回傳 -1

        result = []
        for q in queries:
            result.append(res[q])   # 按原始 queries 順序從 dictionary 取出答案
        return result