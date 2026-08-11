# 0081. Search in Rotated Sorted Array II
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# 難度：Medium
# 類型：Binary Search

# 思路：
# 跟 0033 架構相同，用 nums[middle] 跟 nums[right] 比較判斷哪半邊正常排序，
# 但這題陣列可能有重複值，導致 nums[middle] == nums[right] 時無法判斷哪半邊是正常排序的。
# left 設 0，right 設 len(nums) - 1，用 while left <= right 持續搜尋。
# 每一輪先檢查 nums[middle] 是否等於 target，是的話直接回傳 True。
# 如果 nums[middle] == nums[right]（數值相同、資訊不明確）：
#   因為已經確認 nums[middle] != target，而 nums[right] 跟 nums[middle] 同值，
#   所以 nums[right] 也一定不是 target，可以放心把 right -= 1，排除這個不明確的重複值，
#   下一輪重新判斷。
# 如果 nums[middle] > nums[right]，代表左半邊（left 到 middle）是正常排序的：
#   檢查 target 是否落在 nums[left] 到 nums[middle] 之間，是的話 target 在左半邊，right 移到 middle - 1；
#   否則 target 在右半邊，left 移到 middle + 1。
# 否則（nums[middle] <= nums[right]，但已排除相等情況，所以是 nums[middle] < nums[right]），
# 代表右半邊（middle 到 right）是正常排序的：
#   檢查 target 是否落在 nums[middle] 到 nums[right] 之間，是的話 target 在右半邊，left 移到 middle + 1；
#   否則 target 在左半邊，right 移到 middle - 1。
# 迴圈結束都沒找到就回傳 False。

# Pattern 筆記：
# 這題的 pattern 是旋轉陣列搜尋 + 處理重複值，下次看到「旋轉陣列 + 可能有重複元素」的特徵就用這個方法，
# 並記得當 nums[middle] == nums[right] 時無法判斷哪半邊排序，要先收縮 right 排除這個不明確的值，
# 這也是為什麼這題最壞情況會退化成 O(n)（不再穩定是 O(log n)）。

# Time complexity: O(n) 最壞情況（大量重複值時會退化），平均 O(log n)
# Space complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0  # 搜尋範圍的左邊界
        right = len(nums) - 1  # 搜尋範圍的右邊界
        while left <= right:  # 左右邊界還沒交叉就繼續找
            middle = (left + right) // 2  # 取中間 index
            if nums[middle] == target:  # 找到 target
                return True
            elif nums[middle] == nums[right]:  # 數值相同，無法判斷哪半邊排序
                right -= 1  # 排除這個不明確的重複值
            elif nums[middle] > nums[right]:  # 左半邊是正常排序的
                if nums[left] <= target < nums[middle]:  # target 在左半邊範圍內
                    right = middle - 1
                else:  # target 在右半邊
                    left = middle + 1
            else:  # 右半邊是正常排序的
                if nums[middle] < target <= nums[right]:  # target 在右半邊範圍內
                    left = middle + 1
                else:  # target 在左半邊
                    right = middle - 1
        return False  # 找不到