# 0153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# 難度：Medium
# 類型：Binary Search

# 思路：
# 陣列被旋轉過，不是完全排序的，但可以用 nums[middle] 和 nums[right] 比較來判斷「斷點」（最小值）在哪一半。
# left 設 0，right 設 len(nums) - 1，用 while left < right 持續搜尋（因為 middle 有可能不會被排除，
# 所以用 left < right 避免無限迴圈，迴圈結束時 left 會等於 right，剛好停在最小值的位置）。
# middle 取中間值，比較 nums[middle] 和 nums[right]：
# 如果 nums[middle] > nums[right]，代表 middle 到 right 這段裡藏著斷點（最小值），
# 且 middle 本身一定不是最小值（因為它比 right 還大），所以可以排除 middle，left 移到 middle + 1。
# 否則（nums[middle] <= nums[right]），代表斷點在 left 到 middle 這段（包含 middle 本身，
# middle 有可能就是最小值），所以不能排除 middle，right 移到 middle（不是 middle - 1）。
# 迴圈結束時 left == right，回傳 nums[left] 就是最小值。

# Pattern 筆記：
# 這題的 pattern 是旋轉陣列的 binary search，透過跟 nums[right] 比較大小來判斷斷點位置，
# 下次看到「陣列被旋轉過、不是完全排序」的特徵就用這個方法，並注意某個分支會保留 middle（不 -1/+1），
# 這時候要把迴圈條件改成 while left < right，避免無限迴圈。

# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0  # 搜尋範圍的左邊界
        right = len(nums) - 1  # 搜尋範圍的右邊界
        while left < right:  # left 和 right 還沒相遇就繼續找
            middle = (left + right) // 2  # 取中間 index
            if nums[middle] > nums[right]:  # 斷點在 middle 右邊，middle 本身不是最小值
                left = middle + 1
            else:  # 斷點在 middle 左邊（含 middle），middle 有可能是最小值
                right = middle
        return nums[left]  # left 和 right 相遇的位置就是最小值