# 136. Single Number
# https://leetcode.com/problems/single-number/
# 難度：Easy
# 類型：Bit Manipulation

# 思路：
# 利用 XOR (^) 的特性：
# 1. 任何數字跟自己 XOR，結果是 0（a ^ a = 0）
# 2. 任何數字跟 0 XOR，結果是自己（a ^ 0 = a）
# 3. XOR 滿足交換律和結合律，可以任意重新排列順序
# 把陣列裡所有數字 XOR 在一起，成對出現的數字會互相抵消變成 0
# 最後只剩下落單的那個數字

# Time: O(n)
# Space: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0                  # 初始值是 0，因為任何數字 XOR 0 還是自己

        for n in nums:
            res = n ^ res
            # 把每個數字依序 XOR 進來
            # 成對的數字最終會互相抵消（變成0），落單的數字會保留下來

        return res               # 只出現一次的數字