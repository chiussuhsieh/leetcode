# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/
# 難度：Medium
# 類型：2D DP

# 思路：
# dp[i][j] = 從起點走到 (i,j) 有幾種走法
# 到達 (i,j) 只能從上面 (i-1,j) 或左邊 (i,j-1) 來
# dp[i][j] = dp[i-1][j] + dp[i][j-1]
# base case：第一行和第一列都只有 1 種走法，初始化成 1

# Time: O(m*n)
# Space: O(m*n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):          # 建立 m 行
            row = []                # 每次建立一個新的 row
            for j in range(n):      # 每行有 n 個格子
                row.append(1)       # 全部初始化成 1，處理第一行和第一列的 base case
            dp.append(row)          # 把 row 加進 dp

        for i in range(1, m):       # 從第二行開始，第一行已經是 1
            for j in range(1, n):   # 從第二列開始，第一列已經是 1
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                # 從上面來的走法 + 從左邊來的走法

        return dp[m-1][n-1]         # 終點的走法數量