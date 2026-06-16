# 97. Interleaving String
# https://leetcode.com/problems/interleaving-string/
# 難度：Medium
# 類型：2D DP

# 思路：
# dp[i][j] = s1 前 i 個字元和 s2 前 j 個字元，能不能交錯組成 s3 前 i+j 個字元
# 看 s3 目前處理到的最後一個字元（index = i+j-1）是從哪裡來的：
#   情況1：來自 s1[i-1]，且前面 dp[i-1][j] 也成立
#   情況2：來自 s2[j-1]，且前面 dp[i][j-1] 也成立
# 兩種情況只要一個成立，dp[i][j] 就是 True
# base case：dp[0][0]=True（兩個空字串組成空字串）
# dp[i][0]/dp[0][j] 要逐字檢查順序對不對，不能直接設 True

# Time: O(m*n)
# Space: O(m*n)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False   # 長度不對，s3 不可能由 s1、s2 交錯組成

        # 建立 (m+1) x (n+1) 的 2D 陣列，全部初始化成 False
        dp = []
        for i in range(m + 1):
            row = []
            for j in range(n + 1):
                row.append(False)
            dp.append(row)

        dp[0][0] = True   # 兩個空字串可以組成空字串

        # base case：s2 是空字串，只用 s1 組成 s3 的前 i 個字元
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
            # 前面 i-1 個字元已經對得上，且這個字元也對得上，才是 True

        # base case：s1 是空字串，只用 s2 組成 s3 的前 j 個字元
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                           (dp[i][j-1] and s2[j-1] == s3[i+j-1])
                # 情況1：這個字元來自 s1，且前面交錯成功
                # 情況2：這個字元來自 s2，且前面交錯成功
                # 任一成立，dp[i][j] 就是 True

        return dp[m][n]   # s1 和 s2 能不能完整交錯組成 s3