# 115. Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/
# 難度：Hard
# 類型：2D DP

# 思路：
# dp[i][j] = s 前 i 個字元，有幾種方法選出字元組成 t 前 j 個字元
# 情況1：s[i-1] == t[j-1]，這個字元可以選或不選
#   選：dp[i-1][j-1]（這個字元拿來配對 t[j-1]）
#   不選：dp[i-1][j]（跳過 s 的這個字元，靠前面的湊出 t）
#   dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
# 情況2：s[i-1] != t[j-1]，只能不選這個字元
#   dp[i][j] = dp[i-1][j]
# base case：dp[i][0] = 1（t 是空字串，s 任何前綴都有一種方法湊出空字串：都不選）
#            dp[0][j] = 0（s 是空字串，無法湊出非空的 t），j>0

# Time: O(m*n)
# Space: O(m*n)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dp = []
        for i in range(m + 1):
            row = []
            for j in range(n + 1):
                row.append(0)
            dp.append(row)

        for i in range(m + 1):
            dp[i][0] = 1
            # t 是空字串，不管 s 前 i 個字元是什麼，都只有一種方法：什麼都不選

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    # 選這個字元配對 t[j-1] + 不選這個字元（靠前面湊）
                else:
                    dp[i][j] = dp[i-1][j]
                    # 字元不同，只能跳過 s 的這個字元

        return dp[m][n]