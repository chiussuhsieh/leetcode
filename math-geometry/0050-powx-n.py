# 50. Pow(x, n)
# https://leetcode.com/problems/pow-x-n/
# 難度：Medium
# 類型：Math, Recursion

# 思路：
# 直覺解法是乘 n 次，O(n) 太慢
# Fast Power（快速冪）：每次把次方折半，只需要 O(log n) 次運算
# n 是偶數：x^n = (x^2)^(n/2)，底數平方，次方折半
# n 是奇數：x^n = x * (x^2)^(n//2)，多乘一個 x 處理餘數
# 負數次方：x^(-n) = 1 / x^n，轉成正數次方處理
# base case：n=0，任何數的 0 次方都是 1

# Time: O(log n)
# Space: O(log n)，遞迴堆疊

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1              # base case：0 次方一定是 1

        if n < 0:
            return 1 / self.myPow(x, -n)
            # 負數次方：轉成正數次方，最後取倒數

        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
            # 偶數次方：底數平方，次方折半
            # 例如 x^10 = (x^2)^5

        else:
            return x * self.myPow(x * x, n // 2)
            # 奇數次方：多乘一個 x 處理餘數
            # 例如 x^5 = x * (x^2)^2