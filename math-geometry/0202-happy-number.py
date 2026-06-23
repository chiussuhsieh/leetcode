# 202. Happy Number
# https://leetcode.com/problems/happy-number/
# 難度：Easy
# 類型：Math

# 思路：
# 反覆把每個位數的平方加起來，直到結果是 1（Happy Number）或陷入循環（不是）
# 用 set 記錄出現過的數字，如果同一個數字出現兩次，代表陷入無限循環
# 計算每個位數的平方和：用 % 10 取出最後一位，// 10 去掉最後一位
# 內層 while n 是在取出每個位數，當所有位數都取完後 n 會變成 0 自動停止

# Time: O(log n)
# Space: O(log n)，seen set 存放出現過的數字

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()               # 記錄出現過的數字，用來偵測循環

        while n != 1:              # 還沒到達 1，繼續處理
            if n in seen:
                return False       # 這個數字出現過了，陷入無限循環，不是 Happy Number

            seen.add(n)            # 把這個數字記錄下來

            total = 0
            while n:               # 把 n 的每個位數取出來（n 會逐漸變小直到 0）
                digit = n % 10     # 取出最後一位數字
                total += digit ** 2   # 平方加進 total
                n = n // 10        # 去掉最後一位，準備取下一位

            n = total              # 更新 n 為新的數字，繼續外層 loop

        return True                # n 變成 1，是 Happy Number