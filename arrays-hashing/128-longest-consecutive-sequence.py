# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
# 難度：Medium
# 類型：Array, HashSet
# 思路：
# 把所有數字放進 set，查找是否存在為 O(1)
# iterate numSet，如果 num - 1 不在 set 裡，代表這是 sequence 的頭
# 從頭開始用 while loop 往後找，num += 1 直到找不到為止
# 每次更新 maxCount
# 這樣每個數字只被處理一次，達到 O(n)
# Pattern 筆記：
# 這題的 pattern 是「HashSet + 只從 sequence 的頭開始計算」
# num - 1 不在 set 裡才是頭，避免從中間重複計算
# 下次看到「找最長連續序列且要求 O(n)」就用這個方法
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0
        numSet = set(nums)
        for num in numSet:
            count = 0
            if num - 1 not in numSet:      # 確認是 sequence 的頭
                count = 1
                while num + 1 in numSet:   # 往後找直到找不到為止
                    count += 1
                    num += 1               # 更新 num 繼續往後
                maxCount = max(maxCount, count)
            else:
                continue
        return maxCount