# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# 難度：Easy
# 類型：Array, HashSet
# 思路：
# 建立空 set，iterate array
# 如果 element 不在 set 就加進去
# 如果已經在 set 裡，代表重複，return True
# loop 結束都沒重複就 return False
# Pattern 筆記：
# 這題的 pattern 是「HashSet 查重」
# 下次看到「判斷是否有重複元素」特徵就用這個方法
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for i in range(len(nums)):
            if nums[i] not in numSet:  # 不在 set 裡就加入
                numSet.add(nums[i])
            else:
                return True            # 已存在，代表重複
        return False                   # 沒有重複