# 0035. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# 難度：Easy
# 類型：Binary Search

# 思路：
# 跟 0704 幾乎一樣的 binary search 樣板，用 left 和 right 框住搜尋範圍。
# 用 while left <= right 持續搜尋，middle 取中間值。
# 如果 nums[middle] 剛好等於 target，直接回傳 middle。
# 如果 nums[middle] 比 target 大，right 移到 middle - 1。
# 如果 nums[middle] 比 target 小，left 移到 middle + 1。
# 迴圈結束代表沒找到 target，這時候 left 會停在「比 target 大的第一個元素」的位置，
# 也就是 target 應該被插入的位置，所以回傳 left。

# Pattern 筆記：
# 這題的 pattern 是 binary search 樣板 + 利用迴圈結束時 left 的位置，下次看到「找不到值時要回傳插入位置」的特徵就用這個方法。

# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
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
        return left  # 迴圈結束，left 就是應該插入的位置