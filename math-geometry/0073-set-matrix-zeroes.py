# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/
# 難度：Medium
# 類型：Math, Matrix

# 思路：
# 不能邊掃邊設0，因為新設的0會影響後面的判斷，導致錯誤結果
# 所以分兩步：
# 第一步：掃整個 matrix，用 set 記錄哪些 row 和 col 原本就有 0
# 第二步：再掃一遍整個 matrix，對每一格檢查「它的 row 或 col 有沒有在記錄裡」
#         有的話就設成 0，這樣自然就把整行整列都設成 0 了

# Time: O(m*n)
# Space: O(m+n)，最差情況下每行每列都有 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zero_rows = set()   # 記錄哪些 row 有 0
        zero_cols = set()   # 記錄哪些 col 有 0

        # 第一步：掃一遍，記錄哪些 row 和 col 有 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)   # 這個 row 需要設成 0
                    zero_cols.add(c)   # 這個 col 需要設成 0

        # 第二步：再掃一遍整個 matrix，把對應的行和列設成 0
        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_cols:
                    # 這一格的 row 或 col 有 0，設成 0
                    matrix[r][c] = 0