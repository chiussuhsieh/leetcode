# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/
# 難度：Medium
# 類型：DP（0/1 背包問題）

# 思路：
# 把問題簡化：能不能從陣列裡挑一些數字，湊出 sum(nums) / 2？
# dp[i] = 能不能從陣列裡挑一些數字湊出總和 i（True/False）
# 每個數字只能用一次，所以內層 loop 從右到左，避免重複使用

# Time: O(n * target)
# Space: O(target)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False               # 總和是奇數，不可能分成兩個相等子集

        target = total // 2            # 目標：湊出總和的一半
        dp = [False] * (target + 1)    # dp[i] = 能不能湊出總和 i
        dp[0] = True                   # 湊出 0，不選任何數字，一定可以

        for num in nums:               # 試每個數字
            for i in range(target, num - 1, -1):
                # 從右到左更新，確保每個數字只用一次
                # i 最小走到 num，確保 i - num >= 0

                if dp[i - num]:
                    dp[i] = True
                    # 如果前面能湊出 i - num
                    # 加上這個 num 就能湊出 i

        return dp[target]              # 能不能湊出目標總和