# 1584. Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/
# 難度：Medium
# 類型：Graph (Prim's Algorithm / Minimum Spanning Tree)

# 思路：
# 目標不是找最短路徑，而是用最少的總邊權重，把所有點連成一個連通網路（MST）
# 這是完全圖：任意兩點之間都有邊，權重是 Manhattan distance
# 用 Prim's Algorithm（概念跟 Dijkstra 很像）：
# 1. 從任意一個點開始，用 min heap 找「目前能連到的點裡，成本最小的那條邊」
# 2. 加入這個點，把它的總成本累加進答案
# 3. 重複直到所有點都連起來
# 跟 Dijkstra 的關鍵差異：heap 存的是「這一步邊的成本」，不是「累積距離」
# 因為 MST 關心的是每條邊本身的權重總和，不是從起點走多遠

# Time: O(n^2 log n)
# Space: O(n^2)

import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def manhattan(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
            # 計算兩點間的 Manhattan distance

        heap = [(0, 0)]    # (邊的成本, 點的 index)，從 point 0 開始，成本 0
        visited = set()    # 記錄已經連進網路的點
        total_cost = 0      # 累積總成本

        while heap and len(visited) < n:
            cost, i = heapq.heappop(heap)
            # 取出目前能連到的點裡，成本最小的那個

            if i in visited:
                continue
                # 這個點已經連進網路了，這條邊是多餘的，跳過

            visited.add(i)
            total_cost += cost
            # 把這個點加入網路，累加這條邊的成本

            for j in range(n):
                if j not in visited:
                    dist = manhattan(points[i], points[j])
                    heapq.heappush(heap, (dist, j))
                    # 把 i 到所有還沒連進網路的點的邊，加入 heap
                    # 之後會在裡面找出最小成本的那條

        return total_cost   # 連接所有點需要的最小總成本