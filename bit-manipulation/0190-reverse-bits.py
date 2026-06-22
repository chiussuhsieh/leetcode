# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/
# 難度：Easy
# 類型：Bit Manipulation

# 思路：
# 整數在電腦裡本來就是二進位，不需要額外轉換
# 每次從 n 的最右邊取出一個 bit，放到 res 的最右邊
# 然後 n 右移一位（準備取下一個 bit），res 左移一位（騰出空位給下一個 bit）
# 固定跑 32 次（32-bit 整數）
# 關鍵：res << 1 左移後最右邊一定是 0，用 | 把取出的 bit 放進去
#       0 | 1 = 1，0 | 0 = 0，所以 | 可以用來「放進」bit

# Time: O(32) = O(1)
# Space: O(1)

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0                      # 用來累積反轉後的結果

        for i in range(32):          # 固定跑 32 次，處理 32 個 bit
            bit = n & 1              # 取出 n 最右邊的 bit（0 或 1）
            res = res << 1 | bit     # res 左移一位騰出空位，用 | 把 bit 放進最右邊
            n = n >> 1               # n 右移一位，丟掉剛取出的 bit，準備取下一個

        return res                   # 反轉後的 32-bit 整數