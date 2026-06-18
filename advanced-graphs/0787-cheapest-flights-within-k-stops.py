# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# 難度：Medium
# 類型：Graph (Dijkstra's Algorithm 變形)

# 思路：
# 跟 Network Delay Time 很像，但多了「最多 k 個中轉站」的限制
# 標準 Dijkstra 的 visited 不能直接用，因為「步數少但貴」跟「步數多但便宜」
# 都可能是合法答案，不能只靠花費決定要不要訪問一個節點
# heap 存 (花費, 節點, 已用步數)，因為是 min heap，第一次彈出終點就是最便宜的答案
# 用 best_stops 表剪枝：如果已經有更少步數到過這個節點，現在用更多步數
# 重新走一遍不可能更便宜（min heap 保證花費遞增），直接跳過避免無限擴展

# 卡住的地方：
# 一開始沒有任何剪枝，導致同一個節點被重複擴展太多次，在有環的圖上發生 TLE
# 加上 best_stops 表後解決

# Time: O(E * K * log(E*K))，最差情況下
# Space: O(V + E)

import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)        # 建立鄰接表：key=出發節點, value=[(到達節點, 花費), ...]
        for u, v, w in flights:
            graph[u].append((v, w))

        heap = [(0, src, 0)]    # (累積花費, 目前節點, 已經用的步數)，從起點開始
        best_stops = {}         # 記錄到每個節點，目前已知最少要用幾步

        while heap:
            cost, node, stops = heapq.heappop(heap)
            # 取出目前花費最小的方案（min heap 保證）

            if node == dst:
                return cost
                # 第一次彈出終點，因為 heap 保證花費最小，這就是答案

            if stops > k:
                continue
                # 已經超過允許的中轉站數量，這條路徑不合法，放棄

            if node in best_stops and best_stops[node] <= stops:
                continue
                # 之前已經用更少或相同步數到過這個節點
                # 現在這條路徑步數更多，花費一定不會更好，跳過避免重複擴展

            best_stops[node] = stops
            # 更新：用目前的步數記錄到這個節點

            for neighbor, weight in graph[node]:
                heapq.heappush(heap, (cost + weight, neighbor, stops + 1))
                # 往外擴展，把鄰居加入 heap，步數 +1

        return -1   # heap 空了還沒到終點，無法在限制內到達