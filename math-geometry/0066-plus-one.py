# 66. Plus One
# https://leetcode.com/problems/plus-one/
# 難度：Easy
# 類型：Math

# 思路：
# 把 digits array 轉成整數，直接加一，再轉回 array
# 轉成整數：用 number * 10 + d 的方式，從左到右把每個位數累積進去
# 轉回 array：把整數轉成字串，iterate 每個字元，轉回 int 加進結果
# 這樣不需要處理進位的 edge case（像 999 → 1000），直接讓整數運算處理！

# Time: O(n)
# Space: O(n)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for d in digits:
            number = number * 10 + d
            # 把 array 轉成整數
            # 每次把前面的數字乘以10，再把新的數字加進來
            # 例如 [1,2,3]：0→1→12→123

        number += 1   # 加一，進位的情況（999→1000）自動處理

        array = []
        for d in str(number):     # 把整數轉成字串，才能 iterate 每個位數
            array.append(int(d))  # 每個字元轉回 int，加進結果
        return array