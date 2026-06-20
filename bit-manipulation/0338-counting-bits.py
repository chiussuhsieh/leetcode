# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/
# 難度：Easy
# 類型：Bit Manipulation, DP

# 思路：
# 從 0 開始，逐步往上建表，用「更小的數字」的答案推出現在的答案
# dp[i] = i 的二進位表示法中有幾個 1
# 把 i 的最後一個 bit 拿掉（i >> 1），剩下的數字答案 dp[i>>1] 已經算好了（因為從小到大建表）
# 再加上被拿掉的那個 bit 是不是 1（i % 2，奇數代表是1）
# dp[i] = dp[i >> 1] + (i % 2)
# base case：dp[0] = 0（0 沒有任何 bit 是 1）

# Time: O(n)
# Space: O(n)

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)   # dp[i] = i 的二進位表示法中有幾個 1
                              # dp[0] = 0，已經初始化好了，是 base case

        for i in range(1, n + 1):   # 從 1 開始，逐步往上建到 n
            dp[i] = dp[i >> 1] + (i % 2)
            # i >> 1：把 i 的最後一個 bit 丟掉
            #         剩下的數字一定比 i 小，所以 dp[i >> 1] 已經先被算過了（DP 分解問題的概念）
            # i % 2：檢查被丟掉的那個 bit 是不是 1，奇數代表是1，偶數代表是0

        return dp   # 0 到 n 每個數字的 1 的個數