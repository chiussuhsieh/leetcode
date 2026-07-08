# 26. Remove Duplicates From Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 難度：Easy
# 類型：Two Pointers

# 思路：
# 因為 nums 已經排序過，重複的元素一定會相鄰。
# 用兩個指標：l 負責「下一個要寫入唯一值的位置」，同時也代表「目前為止總共有幾個唯一值」；
# r 負責掃描整個陣列，去跟前一個元素 nums[r-1] 比較。
# l 從 1 開始（因為位置 0 的元素一定是第一個唯一值，不需要額外處理）。
# r 從 1 跑到陣列尾端，只要 nums[r] != nums[r-1]，就代表遇到了新的唯一值，
# 把它寫到 nums[l] 的位置，然後 l += 1。
# 因為 l 已經從 1 起跳，代表位置 0 那個唯一值已經內定算進去了，
# 所以迴圈結束後直接 return l，就是唯一值的總數量，不需要再 +1。

# Pattern 筆記：
# 這題的 pattern 是「快慢指標去重（slow-fast pointer for in-place deduplication）」，
# 下次看到「排序陣列」且「in-place 去除重複、回傳唯一值數量」的特徵就用這個方法。

# Time: O(n)
# Space: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            # 跟前一個元素比較，不一樣就代表是新的唯一值
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l