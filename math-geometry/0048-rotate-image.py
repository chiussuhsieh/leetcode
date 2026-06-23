# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/
# 難度：Medium
# 類型：Math, Matrix

# 思路：
# 順時針旋轉 90 度 = Transpose + 每行左右反轉
# Transpose：把 matrix[i][j] 和 matrix[j][i] 互換，沿對角線翻轉
#   只處理上三角形（j 從 i+1 開始），避免同一對位置被換兩次換回來
# 每行左右反轉：用雙指針，左右兩端往中間靠攏，交換元素
# 兩步合起來就是順時針旋轉 90 度，不需要額外的矩陣（in-place）

# Time: O(n^2)
# Space: O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 第一步：Transpose（轉置）
        for i in range(n):
            for j in range(i + 1, n):
                # j 從 i+1 開始，只處理上三角形
                # 避免同一對位置（i,j）和（j,i）被換兩次換回來
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 第二步：每一行左右反轉
        for i in range(n):
            left, right = 0, n - 1      # 雙指針，從兩端往中間靠攏
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                # 交換左右兩端的元素
                left += 1               # 左指針往右移
                right -= 1              # 右指針往左移