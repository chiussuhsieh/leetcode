# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# 難度：Medium
# 類型：Math

# 思路：
# 用 % 10 取出最後一位數字，// 10 去掉最後一位，反覆操作直到 x 變成 0
# 每次把取出的數字放到 res 的最右邊（res * 10 + digit）
# 前導零不需要特別處理，因為 0 放到 res 最右邊不影響結果
# 負數先用 abs() 轉成正數處理，最後乘回正負號
# 最後檢查是否超出 32-bit 範圍，超出回傳 0

# Time: O(log x)，x 有幾位數就跑幾次
# Space: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1   # 先記錄正負號，abs() 之前就要記錄
        x = abs(x)                    # 轉成正數，方便處理
        res = 0

        while x != 0:                 # x 還有數字沒處理完
            digit = x % 10            # 取出最後一位數字
            x = x // 10              # 去掉最後一位數字
            res = res * 10 + digit    # 把取出的數字放到 res 的最右邊

        return res * sign if res < 2**31 else 0
        # 乘回正負號，如果超出 32-bit 範圍（2^31）回傳 0