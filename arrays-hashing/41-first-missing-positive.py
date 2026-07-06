# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/
# 難度：Hard
# 類型：Array, HashSet
# 思路：
# 把 nums 放進 set
# 從 1 開始，如果 i 在 set 裡就繼續往下找
# 遇到不在 set 裡的就是第一個缺少的正整數
# Pattern 筆記：
# 這題的 pattern 是「HashSet + 從 1 開始線性掃描」
# 下次看到「找最小缺少的正整數」就用這個方法
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet = set(nums)       # 把所有數字放進 set
        i = 1
        while i in numSet:      # 從 1 開始，找到不在 set 裡的就是答案
            i += 1
        return i