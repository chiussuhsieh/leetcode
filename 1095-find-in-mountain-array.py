# 1095. Find in Mountain Array
# https://leetcode.com/problems/find-in-mountain-array/
# 難度：Hard
# 類型：Binary Search

# 思路：
# 這題分三個步驟：先找出峰值 index，再依序在左半邊（遞增區）和右半邊（遞減區）做 binary search。
#
# 第一步：找峰值
# left 設 0，right 設 mountainArr.length() - 1，用 while left < right（因為峰值本身可能是 middle，
# 需要保留它，不能用 +1/-1 跳過）。
# 每一輪比較 mountainArr.get(middle) 跟 mountainArr.get(middle + 1)：
#   如果 middle 比 middle+1 小，代表還在上坡，峰值在右側，left 移到 middle + 1；
#   否則代表已經過了峰值（在下坡），峰值在左側（含 middle 本身），right 移到 middle。
# 迴圈結束時 left == right，就是峰值的 index，存到 peak。
#
# 第二步：判斷 target 落在哪一段
# 用 mountainArr.get(0) <= target <= mountainArr.get(peak) 判斷 target 是否落在左半邊（遞增區）的範圍內。
#
# 第三步：對應區間做標準 binary search
# 如果 target 在左半邊範圍內，在 [0, peak] 這段用標準遞增 binary search（跟 0704 一樣的方向）。
# 否則在 [peak, length-1] 這段做搜尋，但因為這段是遞減的，方向要反過來：
#   如果 get(middle) > target（太大了），要往右找更小的值，left 移到 middle + 1；
#   如果 get(middle) < target（太小了），要往左找更大的值，right 移到 middle - 1。
# 兩段都用 while left <= right（因為都用 middle ± 1 跳過 middle，不保留它）。
# 找到就回傳 middle，都找不到則回傳 -1。
# 題目允許回傳任何一個符合條件的 index，所以先搜左半邊、找不到才搜右半邊即可，不需要比較挑選最小值。

# Pattern 筆記：
# 這題的 pattern 是「先用 binary search 找峰值，再依峰值切成遞增/遞減兩段分別做 binary search」，
# 下次看到「山脈陣列（先增後減）+ 找特定值」的特徵就用這個方法。
# 關鍵是理解：遞減區間一樣可以用 binary search，只是判斷方向要反過來
# （值太大時要往右找、值太小時要往左找，跟標準遞增陣列相反）。

# Time complexity: O(log n)，三次 binary search 各自 O(log n)
# Space complexity: O(1)

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left = 0  # 找峰值的左邊界
        right = mountainArr.length() - 1  # 找峰值的右邊界
        while left < right:  # 左右邊界還沒相遇就繼續找峰值
            middle = (left + right) // 2
            if mountainArr.get(middle) < mountainArr.get(middle + 1):  # 還在上坡
                left = middle + 1
            else:  # 已經過了峰值（在下坡），middle 可能就是峰值
                right = middle
        peak = left  # 峰值的 index

        if mountainArr.get(0) <= target <= mountainArr.get(peak):  # target 在左半邊（遞增區）範圍內
            left = 0
            right = peak
            while left <= right:  # 標準遞增 binary search
                middle = (left + right) // 2
                if mountainArr.get(middle) == target:
                    return middle
                elif mountainArr.get(middle) > target:
                    right = middle - 1
                else:
                    left = middle + 1
        else:  # target 在右半邊（遞減區）
            left = peak
            right = mountainArr.length() - 1
            while left <= right:  # 遞減陣列的 binary search，方向相反
                middle = (left + right) // 2
                if mountainArr.get(middle) == target:
                    return middle
                elif mountainArr.get(middle) > target:  # 太大了，往右找更小的值
                    left = middle + 1
                else:  # 太小了，往左找更大的值
                    right = middle - 1
        return -1  # 都找不到