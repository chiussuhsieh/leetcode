# 2013. Detect Squares
# https://leetcode.com/problems/detect-squares/
# 難度：Medium
# 類型：Math, Hash Map

# 思路：
# 用一個 dictionary 記錄每個點出現幾次
# count 的時候，找「對角點」：
# 給查詢點 (qx, qy)，對角點 (x, y) 必須滿足：
#   1. abs(qy - y) == abs(qx - x)（高度等於寬度，才是正方形）
#   2. x != qx（不能同一列）
#   3. y != qy（不能同一行）
# 找到對角點後，另外兩個角自動是 (x, qy) 和 (qx, y)
# 把三個角的出現次數乘起來，加進結果

# Time: add O(1), count O(n)
# Space: O(n)

from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)   # key=(x,y), value=這個點出現幾次

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1   # 把 point 轉成 tuple 當 key，出現次數 +1

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point

        for x, y in list(self.ptsCount):   # 掃所有已知的點，找對角點
            if (abs(qy - y) != abs(qx - x)) or x == qx or y == qy:
                continue
                # 不符合正方形條件，跳過：
                # abs(qy-y) != abs(qx-x)：高度不等於寬度，不是正方形
                # x == qx：同一列，組不成正方形
                # y == qy：同一行，組不成正方形

            res += self.ptsCount[(x, qy)] * self.ptsCount[(qx, y)] * self.ptsCount[(x, y)]
            # 找到合法的對角點 (x, y)，另外兩個角是 (x, qy) 和 (qx, y)
            # 把三個角的出現次數乘起來（同一個點可能出現多次）
            # 查詢點 (qx, qy) 本身不需要乘，因為題目給定它存在

        return res