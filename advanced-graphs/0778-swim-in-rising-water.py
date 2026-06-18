# 778. Swim in Rising Water
# https://leetcode.com/problems/swim-in-rising-water/
# 難度：Hard
# 類型：Graph (Dijkstra's Algorithm 變形)

# 思路：
# 跟標準 Dijkstra 一樣用 min heap 找最優路徑，但「距離」概念不同：
# 不是累加邊的權重，而是「走這條路徑必須等到的最高水位」
# 走到下一格時，需要的水位 = max(目前已等的水位, 下一格的高度)
# 因為水位必須淹過路徑上的每一格才能走過去，取最大值而不是累加
# 用 visited set 避免重複訪問（因為只找一個固定終點，跟之前找全部節點不同）

# Time: O(n^2 log(n^2))，n^2 個格子，heap 操作
# Space: O(n^2)

import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()                     # 記錄已經訪問過的格子
        heap = [(grid[0][0], 0, 0)]         # (需要等的水位, row, col)，從起點 (0,0) 開始
        visited.add((0, 0))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]   # 上下左右四個方向

        while heap:
            time, r, c = heapq.heappop(heap)
            # 取出目前 heap 裡，需要等的水位最小的格子

            if r == n - 1 and c == n - 1:
                return time
                # 到達右下角終點，min heap 保證這是最少需要等的水位

            for dr, dc in directions:
                nr, nc = r + dr, c + dc        # 計算鄰居座標
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    # 確保鄰居在網格範圍內，且還沒訪問過

                    visited.add((nr, nc))      # 標記成已訪問

                    new_time = max(time, grid[nr][nc])
                    # 走到這個鄰居，需要等的水位
                    # = 目前路徑上已經等到的水位 跟 這個鄰居的高度，取較大的

                    heapq.heappush(heap, (new_time, nr, nc))

        return -1   # 理論上不會發生，網格一定能走到終點