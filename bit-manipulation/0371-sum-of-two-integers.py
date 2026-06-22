# 371. Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/
# 難度：Medium
# 類型：Bit Manipulation

# 思路：
# 不能用 + 或 -，用 bit 操作模擬加法
# 加法拆成兩個部分：
# 1. 不考慮進位的加法：用 XOR (^)，相同的 bit 抵消，不同的留下
# 2. 進位的部分：用 AND (&) 找出兩個都是1的位置，再左移一位（進位往左移）
# 重複這兩個操作，直到沒有進位為止（b == 0）
#
# Python 特殊問題：Python 整數沒有 32-bit 限制，負數處理會出問題
# 解決方法：用 mask = 0xFFFFFFFF（32個1）強制限制在 32-bit 範圍內
# 最後如果結果超過 32-bit 最大正數（0x7FFFFFFF），代表是負數，要轉換回來

# Time: O(1)，最多跑 32 次
# Space: O(1)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF          # 32個1，用來強制限制在 32-bit 範圍內

        while b != 0:              # 還有進位，繼續處理
            carry = ((a & b) << 1) & mask
            # a & b：找出兩個都是1的位置（這些位置會產生進位）
            # << 1：進位往左移一位
            # & mask：限制在 32-bit 範圍內，避免 Python 無限增長

            a = (a ^ b) & mask
            # a ^ b：不考慮進位的加法（相同的抵消，不同的留下）
            # & mask：限制在 32-bit 範圍內

            b = carry              # 把進位當成下一輪要加的數字，繼續處理

        if a > 0x7FFFFFFF:
            # 0x7FFFFFFF = 32-bit 最大正數（01111111111111111111111111111111）
            # 如果 a 超過這個值，代表最高位是1，這是個負數
            a = ~(a ^ mask)
            # a ^ mask：把 32-bit 以內的 bit 全部反轉
            # ~(...)：Python 的取反操作，轉換回 Python 的負數表示

        return a