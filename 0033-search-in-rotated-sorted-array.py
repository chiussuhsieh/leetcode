# 0033. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 難度：Medium
# 類型：Binary Search

# 思路：
# 陣列被旋轉過，用 nums[middle] 跟 nums[right] 比較，判斷左半邊還是右半邊是正常排序的。
# left 設 0，right 設 len(nums) - 1，用 while left <= right 持續搜尋。
# 每一輪先檢查 nums[middle] 是否等於 target，是的話直接回傳 middle。
# 如果 nums[middle] > nums[right]，代表左半邊（left 到 middle）是正常排序的：
#   檢查 target 是否落在 nums[left] 到 nums[middle] 之間，是的話代表 target 在左半邊，right 移到 middle；
#   否則代表 target 在右半邊，left 移到 middle + 1。
# 否則（nums[middle] <= nums[right]），代表右半邊（middle 到 right）是正常排序的：
#   檢查 target 是否落在 nums[middle] 到 nums[right] 之間，是的話代表 target 在右半邊，left 移到 middle + 1；
#   否則代表 target 在左半邊，right 移到 middle - 1。
# 因為每輪一開始就先排除了 nums[middle] == target 的情況，所以後面的分支都可以放心用 middle + 1 / middle - 1
# 完全跳過 middle，不需要像 0153 那題保留它。
# 迴圈結束都沒找到就回傳 -1。

# Pattern 筆記：
# 這題的 pattern 是旋轉陣列搜尋 target，先判斷哪一半正常排序，再檢查 target 是否落在該範圍內來決定方向，
# 下次看到「旋轉陣列 + 找特定 target」的特徵就用這個方法。

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
            elif nums[middle] > nums[right]:  # 左半邊是正常排序的
                if nums[left] <= target < nums[middle]:  # target 在左半邊範圍內
                    right = middle
                else:  # target 在右半邊
                    left = middle + 1
            else:  # 右半邊是正常排序的
                if nums[middle] <= target <= nums[right]:  # target 在右半邊範圍內
                    left = middle + 1
                else:  # target 在左半邊
                    right = middle - 1
        return -1  # 找不到