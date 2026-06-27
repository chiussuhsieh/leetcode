# 27. Remove Element
# https://leetcode.com/problems/remove-element/
# 難度：Easy
# 類型：Array
# 思路：
# 用指針 k 記錄「下一個可寫入位置」
# iterate 整個 array，遇到不等於 val 的元素就覆蓋到 nums[k]，k += 1
# 最後 k 就是移除後的長度，前 k 個元素即為結果
# Pattern 筆記：
# 這題的 pattern 是「單指針覆蓋」
# 下次看到「in-place 過濾元素、把符合條件的元素往前收集」就用這個方法
# 用一個指針 k 同時當作寫入位置和最終長度，不符合條件的直接跳過
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0                          # k = 下一個可寫入位置，也是最終長度
        for i in range(len(nums)):
            if nums[i] == val:
                continue               # 等於 val，跳過不處理
            else:
                nums[k] = nums[i]      # 不等於 val，覆蓋到 k 的位置
                k += 1                 # 下一個可寫入位置往後移
        return k                       # 前 k 個元素即為結果