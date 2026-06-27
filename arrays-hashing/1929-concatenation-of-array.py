# 1929. Concatenation of Array
# https://leetcode.com/problems/concatenation-of-array/
# 難度：Easy
# 類型：Array

# 思路：
# 直接把 nums 加到自己後面，Python 的 += 會把兩個 list 合併
# 不需要額外建立新的陣列

# Pattern 筆記：
# 這題的 pattern 是「Array 自我複製」
# 下次看到「把陣列接在自己後面」或「重複陣列兩次」就用 nums += nums

# Time: O(n)
# Space: O(n)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums += nums   # 把 nums 接在自己後面，直接擴充兩倍
        return nums