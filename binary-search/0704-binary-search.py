# 0704. Binary Search
# https://leetcode.com/problems/binary-search/
# 難度：Easy
# 類型：Binary Search

# 思路：
# 用 left 和 right 兩個指標框住搜尋範圍，一開始 left 是 0，right 是陣列最後一個 index。
# 用 while left <= right 讓範圍持續往下搜尋，middle 取 left 和 right 的中間值。
# 如果 nums[middle] 剛好等於 target，直接回傳 middle。
# 如果 nums[middle] 比 target 大，代表 target 在左半邊，把 right 移到 middle - 1。
# 如果 nums[middle] 比 target 小，代表 target 在右半邊，把 left 移到 middle + 1。
# 迴圈結束都沒找到就回傳 -1。

# Pattern 筆記：
# 這題的 pattern 是 binary search 基礎樣板，下次看到「已排序陣列 + 找特定值」的特徵就用這個方法。

# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0  # 搜尋範圍的左邊界
        right = len(nums) - 1  # 搜尋範圍的右邊界
        while left <= right:  # 左右邊界還沒交叉就繼續找
            middle = (left + right) // 2  # 取中間 index
            if nums[middle] == target:  # 找到 target
                return middle
            elif nums[middle] > target:  # target 在左半邊
                right = middle - 1
            else:  # target 在右半邊
                left = middle + 1
        return -1  # 找不到