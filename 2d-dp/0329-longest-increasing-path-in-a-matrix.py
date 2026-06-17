# 329. Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# 難度：Hard
# 類型：2D DP + DFS + Memoization

# 思路：
# dp[r][c] = 從格子 (r,c) 出發，最長的遞增路徑長度
# 用 DFS 往四個方向擴展，只走數字比當前大的格子
# 用 memoization 記住每個格子已經算過的結果，避免重複計算
# 對每個格子都跑一次 DFS，取全局最大值

# Time: O(m*n)，每個格子只計算一次
# Space: O(m*n)，memoization + 遞迴堆疊

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}   # key=(r,c)，value=從這格出發最長的遞增路徑長度

        def dfs(r, c, prevVal):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prevVal:
                return 0   # 超出邊界，或數字沒有變大，這條路走不通

            if (r, c) in dp:
                return dp[(r, c)]   # 已經算過，直接回傳

            res = 1   # 至少包含自己這一格
            # 往四個方向探索，取最長的那條路徑 +1（+1 是因為加上自己這一格）
            res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c-1, matrix[r][c]))

            dp[(r, c)] = res
            return res

        best = 0
        for r in range(ROWS):
            for c in range(COLS):
                best = max(best, dfs(r, c, -1))
                # 對每個格子都跑一次 DFS，prevVal=-1 確保第一步一定能走

        return best