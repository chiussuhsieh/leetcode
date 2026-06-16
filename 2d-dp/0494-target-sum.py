# 494. Target Sum
# https://leetcode.com/problems/target-sum/
# 難度：Medium
# 類型：2D DP（轉換成子集合問題）

# 思路：
# 把「每個數字選+或-」轉換成「分成正數集合 P 和負數集合 N」
# P - N = target，P + N = sum(nums)
# 兩式相加：2P = target + sum(nums) → P = (target + sum(nums)) / 2
# 問題變成：從 nums 選一些數字，湊出總和 P，有幾種方法？
# 跟 Partition Equal Subset Sum 一樣，每個數字只能用一次，內層 loop 從右到左

# Time: O(n * P)
# Space: O(P)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if (target + total) % 2 != 0 or target > total or target < -total:
            return 0
            # P 算出來不是整數，或 target 超出 nums 能組合出的範圍，無解

        P = (target + total) // 2   # 正數集合需要湊出的總和

        dp = [0] * (P + 1)          # dp[i] = 湊出總和 i 有幾種方法
        dp[0] = 1                    # 湊出 0，一種方法：什麼都不選

        for num in nums:                        # 每個數字只能用一次
            for i in range(P, num - 1, -1):      # 從右到左，避免同一個數字被重複使用
                dp[i] += dp[i - num]
                # 湊出 i 的方法數，累加上「用這個 num，從 i-num 湊過來」的方法數

        return dp[P]   # 湊出 P 的方法數，就是答案