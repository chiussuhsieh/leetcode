# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# 難度：Easy
# 類型：DP

# 題目：
# 爬 n 階樓梯，每次可以爬 1 或 2 階，有幾種方法？

# 思路：
# 

# 類似 Fibonacci，f(n) = f(n-1) + f(n-2)
# 因為到第 n 階只能從 n-1 或 n-2 跳上來
# 可以創個ways array 用來儲存到每一階有幾種方法，長度為n+1（index用來對應每個階梯，第一個index是0）
# for loop 後兩階相加除存進ways[i]

# Time: O(n)
# Space: O(1)

# 卡住的地方／犯的錯：
# 

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        return ways[n]