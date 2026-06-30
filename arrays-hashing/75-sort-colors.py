# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/
# 難度：Medium
# 類型：Array, Two Pointers
# 思路：
# 用三個指針 l、r、i
# l 記錄下一個 0 要放的位置，r 記錄下一個 2 要放的位置，i 掃描整個 array
# 遇到 0 跟 l swap，l 和 i 都右移
# 遇到 2 跟 r swap，r 左移，i 不動（換來的數字還沒檢查過）
# 遇到 1 直接跳過，i 右移
# 當 i > r 時結束
# Pattern 筆記：
# 這題的 pattern 是「Dutch National Flag Algorithm（三指針）」
# l 左邊全是 0，r 右邊全是 2，l 到 i 之間全是 1
# 遇到 0 → 跟 l swap，l 和 i 右移
# 遇到 2 → 跟 r swap，r 左移，i 不動（換來的還沒檢查）
# 遇到 1 → i 右移
# 下次看到「只有三種值需要 in-place 分類」就用這個方法
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0
        r = len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]  # 跟左邊 swap
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]  # 跟右邊 swap
                r -= 1
                # i 不動，因為換來的數字還沒檢查過
            else:
                i += 1                                # 遇到 1，直接跳過