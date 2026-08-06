# 0074. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
# 難度：Medium
# 類型：Binary Search

# 思路：
# 因為矩陣每一列由左到右遞增，且每一列的第一個數字都比上一列的最後一個數字大，
# 整個矩陣其實可以看成一個攤平的一維陣列，直接對這個攤平後的陣列做 binary search。
# 先算出 ROWS 和 COLS，left 設 0，right 設 ROWS * COLS - 1（攤平後的最大 index）。
# 用 while left <= right 持續搜尋，middle 取中間值（攤平後的 index）。
# 用 middle // COLS 反推出對應的列數 r（跨過了幾個完整的列），
# 用 middle % COLS 反推出對應的行數 c（在這一列裡的第幾個位置）。
# 如果 matrix[r][c] 剛好等於 target，回傳 True。
# 如果 matrix[r][c] 比 target 大，right 移到 middle - 1。
# 如果 matrix[r][c] 比 target 小，left 移到 middle + 1。
# 迴圈結束都沒找到就回傳 False。

# Pattern 筆記：
# 這題的 pattern 是把 2D 矩陣攤平成 1D 做 binary search，下次看到「2D 矩陣整體具有排序特性（不是每列各自獨立排序）」的特徵就用這個方法，
# 並注意用 middle // COLS 求列數、middle % COLS 求行數（不是用 ROWS）。

# Time complexity: O(log(ROWS * COLS))
# Space complexity: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)  # 矩陣的列數
        COLS = len(matrix[0])  # 矩陣的行數
        left = 0  # 攤平後的搜尋範圍左邊界
        right = ROWS * COLS - 1  # 攤平後的搜尋範圍右邊界
        while left <= right:  # 左右邊界還沒交叉就繼續找
            middle = (left + right) // 2  # 攤平後的 index
            r = middle // COLS  # 反推出列數
            c = middle % COLS  # 反推出行數
            if matrix[r][c] == target:  # 找到 target
                return True
            elif matrix[r][c] > target:  # target 在左半邊
                right = middle - 1
            else:  # target 在右半邊
                left = middle + 1
        return False  # 找不到