# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/
# 難度：Medium
# 類型：DP

# 題目：
# 房子排成圓形，第一間和最後一間是鄰居，不能搶相鄰的房子，求最大金額

# 思路：
# 圓形問題拆成兩個線性問題：
# 1. 不搶第一間：對 nums[1:] 跑一次 House Robber
# 2. 不搶最後一間：對 nums[:-1] 跑一次 House Robber
# 取兩者較大的就是答案

# Time: O(n), Space: O(n)

# 卡住的地方：
# 把圓形拆成兩個線性子問題的思路，直接複用 House Robber 的解法

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.robLinear(nums[1:]), self.robLinear(nums[:-1]))
    
    def robLinear(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        if n <= 2:                              # 兩間以內，選較大的
            return max(dp[0], dp[1])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            # 搶第 i 間：nums[i] + dp[i-2]
            # 不搶第 i 間：dp[i-1]
        return dp[n-1]