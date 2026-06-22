# 268. Missing Number
# https://leetcode.com/problems/missing-number/
# 難度：Easy
# 類型：Bit Manipulation, XOR

# 思路：
# 跟 Single Number 一樣，利用 XOR 的特性：成對出現的數字會互相抵消
# 把「應該要有的數字 0~n」和「陣列裡實際的數字」全部 XOR 在一起
# 出現兩次的數字會抵消，只有缺少的那個數字只出現一次，會被保留下來
# 技巧：i 同時扮演兩個角色：loop 的 index 和「應該存在的數字 0~n-1」
# 先把 n（len(nums)）放進 res，再用一個 loop 同時 XOR 兩組數字

# Time: O(n)
# Space: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)          # 先把 n 放進去（range(n) 不包含 n，要手動補上）

        for i in range(len(nums)):
            res ^= i ^ nums[i]
            # i：「應該要有的數字 0~n-1」，跟 res XOR
            # nums[i]：「陣列裡實際的數字」，跟 res XOR
            # 成對出現的數字會互相抵消，缺少的數字只出現一次，最後會被保留

        return res               # 缺少的那個數字