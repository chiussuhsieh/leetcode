# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# 難度：Medium
# 類型：DP

# 思路：
# 從右到左建 DP
# LIS[i] = 以 nums[i] 為開頭的最長遞增子序列長度
# 對每個 i，往右看所有 j，找比 nums[i] 大的元素接上去
# LIS[i] = max(LIS[i], 1 + LIS[j]) (if nums[i] < nums[j])

# Time: O(n^2)，兩層 loop
# Space: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        # 每個元素自己就是長度 1 的序列
        # 初始化成 1，因為最短就是 1
        for i in range(len(nums)-1, -1, -1):
            # 從右到左遍歷，確保算 LIS[i] 時右邊的值都已經算好
            for j in range(i + 1, len(nums)):
                 # 看 i 右邊所有元素，找可以接在 nums[i] 後面的
                 if nums[i] < nums[j]:
                     # nums[i] < nums[j]：nums[j] 可以接在 nums[i] 後面
                     LIS[i] = max(LIS[i], 1 + LIS[j])
                    # 1 = nums[i] 自己
                    # LIS[j] = 以 nums[j] 開頭的最長序列
                    # 取目前最大值
        return max(LIS)
    # 最長序列不一定從 index 0 開始，所以取整個 LIS 的最大值
        
