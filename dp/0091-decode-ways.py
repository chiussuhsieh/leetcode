# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/
# 難度：Medium
# 類型：DP

# 思路：
# 跟 Climbing Stairs 一樣，每次可以解碼 1 個或 2 個數字
# dp[i] = 前 i 個字元有幾種解碼方式
# dp[i] += dp[i-1]  如果最後一個字元有效（1-9）
# dp[i] += dp[i-2]  如果最後兩個字元有效（10-26）

# Time: O(n)
# Space: O(n)

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1) # dp[i] = 前 i 個字元有幾種解碼方式
        dp[0] = 1 # 空字串有一種解碼方式（base case）
        dp[1] = 0 if s[0] == '0' else 1 # 第一個字元是 '0' 無法解碼，否則有 1 種

        for i in range(2, n + 1): # 從第 2 個字元開始，逐步建到 n
            one = s[i - 1] # 取最後一個字元（單獨解碼）
            two = s[i-2:i] # 取最後兩個字元（一起解碼）

            if one != '0': # 單個字元有效（1-9），繼承前 i-1 個字元的所有解碼方式
                dp[i] += dp[i-1]

            if 1 <= two <= '26': # 兩個字元有效（10-26），繼承前 i-2 個字元的所有解碼方式
                dp[i] += dp[i-2]
        return dp[n] # 整個字串的解碼方式總數