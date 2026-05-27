# 678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/
# 難度：Medium
# 類型：Greedy

# 思路：
# 追蹤「未配對的左括號數量」的範圍 [leftMin, leftMax]
# 因為星號有三種可能，所以用範圍而不是單一值
# leftMin：最少有幾個未配對的左括號（星號盡量當右括號或空）
# leftMax：最多有幾個未配對的左括號（星號盡量當左括號）
# leftMax < 0：就算星號全當左括號，還是有多餘的右括號配不到 → False
# leftMin < 0：星號當右括號用太多了，可以選擇當空字串，歸零就好
# 最後 leftMin == 0：所有左括號都有可能被配對完

# Time: O(n)
# Space: O(1)

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0 # 未配對左括號數量的範圍 [leftMin, leftMax]
        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
                # 確定是左括號，未配對數量一定 +1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
                # 確定是右括號，消耗一個左括號，未配對數量一定 -1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
                # * 有三種可能：
                # 當 ) 或空：leftMin -1（最少情況）
                # 當 (：leftMax +1（最多情況）

            if leftMax < 0:
                return False # 就算 * 全當 (，還是有多餘的 ) 配不到
            if leftMin < 0:
                leftMin = 0 # 負數沒有意義，* 選擇當空字串，歸零

        return leftMin == 0 # 所有 ( 都有可能被配對完