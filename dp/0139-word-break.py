# 139. Word Break
# https://leetcode.com/problems/word-break/
# 難度：Medium
# 類型：DP

# 思路：
# 跟 Coin Change 一樣，試每個單字看能不能拼出前 i 個字元
# dp[i] = 前 i 個字元能不能被單字表完整拼出來（True/False）
# 對每個位置 i，試每個單字，看結尾這段是不是這個單字，且前面能不能拼出來

# Time: O(n * m)，n = len(s)，m = len(wordDict)
# Space: O(n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1) # dp[i] = 前 i 個字元能不能拼出來
        dp[0] = True # 空字串一定能拼出來（base case）

        for i in range(1, n + 1):  # 從第 1 個字元開始，逐步建到 n
            for word in wordDict: # 試每個單字
                l = len(word) # 這個單字的長度
                if i - l >= 0 and dp[i - l] and s[i - l: i] == word:
                    # i - l >= 0：確保不會超出範圍
                    # dp[i-l]：前面那段能不能拼出來
                    # s[i-l:i] == word：結尾這段是不是這個單字
                    dp[i] = True # 三個條件都滿足，dp[i] 可以拼出來
                    break # 已經找到一種拼法，不用再試其他單字
        return dp[n] # 整個字串能不能拼出來