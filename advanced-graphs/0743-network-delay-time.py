# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/
# 難度：Medium
# 類型：Graph (Dijkstra's Algorithm)

# 思路：
# 從起點 k 出發，找到「到所有節點的最短距離」
# 用 Dijkstra 演算法：每次都先確定目前已知距離最小的節點
# 因為距離只會越走越長，min heap 第一次彈出某個節點時，那個距離一定是最短的
# 確定一個節點的最短距離後，往外擴展更新它鄰居的距離（加入 heap）
# heap 裡可能同時存在「同一節點、不同距離」的項目，用 visited 過濾掉較大的重複項
# 最後答案 = 所有節點最短距離裡的最大值（因為要等最慢收到的那個）
# 如果有節點到不了（visited 數量 != n），回傳 -1

# Time: O(E log E)，E 是邊數，heap 操作
# Space: O(V + E)

import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)        # key=節點, value=[(鄰居, 距離), ...]
        for u, v, w in times:
            graph[u].append((v, w))      # 建立鄰接表

        heap = [(0, k)]       # (距離, 節點)，從起點 k 開始，距離 0
        visited = {}          # key=節點, value=確定的最短距離

        while heap:
            time, node = heapq.heappop(heap)
            # 取出目前 heap 裡距離最小的節點
            # min heap 保證第一次彈出某節點時，距離一定是最短的

            if node in visited:
                continue
                # 已經確定過這個節點的最短距離了，現在這個是較大的重複項，跳過

            visited[node] = time
            # 確定這個節點的最短距離（第一次被彈出，保證是最短的）

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (time + weight, neighbor))
                    # 透過 node 往外擴展，更新鄰居的可能距離
                    # 只加入還沒確定的節點，已確定的不用再更新

        if len(visited) != n:
            return -1
            # 不是所有節點都能到達，無法讓全部節點收到訊號

        return max(visited.values())
        # 所有節點最短距離裡的最大值，就是讓全部節點收到訊號需要的時間