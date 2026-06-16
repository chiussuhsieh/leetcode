# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/
# 難度：Medium
# 類型：2D DP

# 思路：
# dp[i][j] = 把 word1 前 i 個字元變成 word2 前 j 個字元，最少需要幾次操作
# 情況1：word1[i-1] == word2[j-1]，字元相同不需要操作，dp[i][j] = dp[i-1][j-1]
# 情況2：字元不同，三種操作選一個取最少：
#   刪除：dp[i-1][j] + 1（word1 少一個字元）
#   插入：dp[i][j-1] + 1（word2 少一個字元要配對）
#   替換：dp[i-1][j-1] + 1（兩邊都少一個字元）
# base case：
#   dp[i][0] = i，word2 是空字串，word1 要刪 i 次變空字串
#   dp[0][j] = j，word1 是空字串，要插入 j 次變成 word2

# Time: O(m*n)
# Space: O(m*n)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # 建立 (m+1) x (n+1) 的 2D 陣列，全部先初始化成 0
        dp = []
        for i in range(m + 1):
            row = []
            for j in range(n + 1):
                row.append(0)
            dp.append(row)

        for i in range(m + 1):
            dp[i][0] = i
            # word2 是空字串，把 word1 前 i 個字元變空字串，要刪除 i 次

        for j in range(n + 1):
            dp[0][j] = j
            # word1 是空字串，要插入 j 次才能變成 word2 前 j 個字元

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    # 字元相同，不需要操作，直接繼承左上角的結果
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    # 刪除、插入、替換，三種操作取最少的，再加上這次操作本身 +1

        return dp[m][n]   # word1 完整變成 word2 所需的最少操作數