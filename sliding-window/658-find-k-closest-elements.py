# 658. Find K Closest Elements
# https://leetcode.com/problems/find-k-closest-elements/
# 難度: Medium
# Type: Sliding Window (雙指針收縮,已排序陣列)

# 思路:
# left、right 指針一開始框住整個陣列(left=0, right=len(arr)-1),
# 持續收縮窗口,直到窗口大小(right-left+1)剛好等於 k。
# 每次收縮時,比較 arr[left] 和 arr[right] 離 x 的距離:
#   若 arr[left] 的距離 <= arr[right] 的距離,代表 right 端該被移除,right -= 1
#   (距離相等時優先保留較小的 arr[left],所以移除 right 這端)
#   否則移除 left 端,left += 1
# 收縮完成後,窗口大小已確定等於 k,直接用 arr[left:right+1] 切出結果。

# Pattern 筆記:
# 這題的 pattern 是「雙指針從兩端向內收縮,適用於已排序陣列」,
# 下次看到「已排序陣列 + 找連續 k 個元素滿足某個最佳條件」的題目,
# 就可以用「left、right 從兩端出發,比較兩端優劣,移除較差的一端」這個技巧。

# Time complexity: O(n - k),等同於 O(n),收縮次數最多是 n-k 次
# Space complexity: O(k),計入輸出結果所佔的空間;若只算額外空間則是 O(1)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1  # 左右指針一開始框住整個陣列

        while right - left + 1 != k:  # 持續收縮,直到窗口大小剛好等於 k
            if abs(arr[left] - x) <= abs(arr[right] - x):  # left 端離 x 較近(或距離相等)
                right -= 1  # 移除 right 端,保留較小的 arr[left]
            else:
                left += 1  # 否則移除 left 端

        res = arr[left: right + 1]  # 窗口大小已確定為 k,切出結果
        return res  # 回傳離 x 最近的 k 個數字