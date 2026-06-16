# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
# 難度：Medium
# 類型：2D DP

# 思路：
# dp[i][j] = text1 前 i 個字元和 text2 前 j 個字元的最長共同子序列長度
# 兩種情況：
# 1. text1[i-1] == text2[j-1]：找到共同字元，dp[i][j] = dp[i-1][j-1] + 1
# 2. text1[i-1] != text2[j-1]：跳過 text1 或 text2 的當前字元，取較大的
#    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# base case：i=0 或 j=0 代表空字串，LCS = 0，初始化成 0

# Time: O(m*n)
# Space: O(m*n)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # 建立 (m+1) x (n+1) 的 2D 陣列，全部初始化成 0
        # 多一行一列處理空字串的 base case
        dp = []
        for i in range(m + 1):
            row = []
            for j in range(n + 1):
                row.append(0)
            dp.append(row)

        for i in range(1, m + 1):       # 從第一個字元開始，i=0 是空字串
            for j in range(1, n + 1):   # 從第一個字元開始，j=0 是空字串
                if text1[i-1] == text2[j-1]:
                    # 當前字元相同，找到一個共同字元
                    # i-1 是因為 dp 多了一行，i=1 對應 text1[0]
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # 當前字元不同，跳過其中一個，取較大的
                    # dp[i-1][j]：跳過 text1 的當前字元
                    # dp[i][j-1]：跳過 text2 的當前字元
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]     # 整個 text1 和 text2 的最長共同子序列長度