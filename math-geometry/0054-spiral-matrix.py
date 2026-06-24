# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# 難度：Medium
# 類型：Math, Matrix

# 思路：
# 用四個邊界（top, bottom, left, right）控制螺旋的範圍
# 每次走完一條邊，就把對應的邊界往內縮
# 順序：top 行（左→右）→ right 列（上→下）→ bottom 行（右→左）→ left 列（下→上）
# 走 bottom 行和 left 列之前要額外檢查邊界
# 因為 top 和 right 已經更新，可能已經超過 bottom 和 left，會重複走已經走過的邊

# Time: O(m*n)
# Space: O(m*n)，結果陣列

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix) - 1      # 上下邊界
        left, right = 0, len(matrix[0]) - 1   # 左右邊界

        while top <= bottom and left <= right:  # 邊界還沒交叉，繼續走

            # 走 top 行（左→右）
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1                            # top 往內縮

            # 走 right 列（上→下）
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1                          # right 往內縮

            # 走 bottom 行（右→左）
            if top <= bottom:                   # 確認 top 沒有超過 bottom（避免重複走）
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1                     # bottom 往內縮

            # 走 left 列（下→上）
            if left <= right:                   # 確認 left 沒有超過 right（避免重複走）
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1                       # left 往內縮

        return res