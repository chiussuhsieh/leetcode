# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
# 難度：Medium
# 類型：Array, HashSet
# 思路：
# 分三次檢查：row、col、3x3 方格
# 每次用 set 記錄出現過的數字，遇到 "." 跳過，發現重複就 return False
# 3x3 方格用 (r // 3, c // 3) 作為 key 識別哪個小方格
# Pattern 筆記：
# 這題的 pattern 是「HashSet 分別檢查 row、col、3x3 方格」
# 用 (r // 3, c // 3) 作為 key 識別哪個小方格
# 下次看到「需要同時驗證多個維度是否有重複」就用這個方法
# Time: O(1)，固定 9x9
# Space: O(1)，固定 9x9

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            rowSet = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowSet:
                    return False
                else:
                    rowSet.add(board[r][c])
        for c in range(9):
            colSet = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in colSet:
                    return False
                else:
                    colSet.add(board[r][c])
        boardMap = {}
        for r in range(9):
            for c in range(9):
                boardKey = (r // 3, c // 3)       # 識別哪個 3x3 小方格
                if board[r][c] == ".":
                    continue
                if boardKey not in boardMap:
                    boardMap[boardKey] = set(board[r][c])  # 初始化 set
                else:
                    if board[r][c] in boardMap[boardKey]:
                        return False
                    else:
                        boardMap[boardKey].add(board[r][c])
        return True




