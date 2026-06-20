# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/
# 難度：Easy
# 類型：Bit Manipulation

# 思路：
# 二進位數字中，每個 bit 是 0 或 1
# "set bit" 的意思是這個 bit 的值是 1
# 要算有幾個 1，可以每次檢查最後一個 bit，然後把整個數字往右移一位，繼續檢查下一個
# n % 2：除以2取餘數，奇數代表最後一個 bit 是1，偶數代表是0（連接到熟悉的數學概念）
# n >> 1：右移一位，把已經檢查過的最後一個 bit 丟掉，準備檢查下一個
# 重複直到 n 變成 0（所有 bit 都檢查完了）

# Time: O(32)，固定 32 個 bit，視為 O(1)
# Space: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0                  # 記錄有幾個 bit 是 1

        while n:                 # n 不是 0，代表還有 bit 沒檢查完
            res += n % 2
            # 檢查最後一個 bit：奇數代表是1，加進 res；偶數代表是0，加0沒差

            n = n >> 1
            # 把整個數字往右移一位，丟掉剛檢查過的最後一個 bit
            # 下一輪檢查的就是原本「倒數第二個」的 bit

        return res                # 總共有幾個 bit 是 1