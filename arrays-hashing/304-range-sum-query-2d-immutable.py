# 304. Range Sum Query 2D Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/
# 難度：Medium
# 類型：Array, Matrix, Prefix Sum
# 思路：
# 預先建好 sumMat，sumMat[r][c] = 從 (0,0) 到 (r-1,c-1) 的矩形總和
# 每一格 = 這一行橫向累積總和(prefix) + 正上方格子(above)
# sumRegion 用四個角落加減：bottomRight - above - left + topLeft
# 用 padding（多一行一列全為 0）避免 edge case
# Pattern 筆記：
# 這題的 pattern 是「2D Prefix Sum」
# __init__ 預先建好 prefix sum matrix，sumRegion 用加減法 O(1) 回傳答案
# 下次看到「多次查詢 2D 矩形區域總和」就用這個方法
# Time: O(m*n) 建立 sumMat，O(1) 查詢
# Space: O(m*n)

class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]  # padding
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]                    # 這一行橫向累積總和
                above = self.sumMat[r][c + 1]             # 正上方格子
                self.sumMat[r + 1][c + 1] = prefix + above  # 完整矩形總和

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1  # 對應 padding
        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1 - 1][col2]
        left = self.sumMat[row2][col1 - 1]
        topLeft = self.sumMat[row1 - 1][col1 - 1]
        return bottomRight - above - left + topLeft