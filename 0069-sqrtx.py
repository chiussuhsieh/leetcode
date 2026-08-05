# 0069. Sqrt(x)
# https://leetcode.com/problems/sqrtx/
# 難度：Easy
# 類型：Binary Search

# 思路：
# 這題答案的可能範圍是 0 到 x，所以 left 設 0，right 設 x，在這個「答案空間」裡做 binary search。
# 用 while left <= right 持續搜尋，middle 取中間值，用 middle ** 2 跟 x 比較大小來判斷方向。
# 如果 middle 平方大於 x，代表猜大了，right 移到 middle - 1。
# 否則（包含小於或等於的情況）代表猜的還不夠大，left 移到 middle + 1。
# 因為答案要無條件捨去，不一定會剛好等於整數解，所以迴圈結束後不是回傳 left，而是回傳 right，
# 因為 right 停在的位置就是「最後一個平方不超過 x 的數字」，也就是無條件捨去後的答案。

# Pattern 筆記：
# 這題的 pattern 是 binary search on answer space（在答案的可能範圍上做搜尋，而不是在陣列裡搜尋），
# 下次看到「答案本身具有單調性、且要無條件捨去或取整數邊界」的特徵就用這個方法，並注意迴圈結束後要回傳 right 而不是 left。

# Time complexity: O(log x)
# Space complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0  # 答案可能範圍的下界
        right = x  # 答案可能範圍的上界
        while left <= right:  # 左右邊界還沒交叉就繼續找
            middle = (left + right) // 2  # 取中間值作為猜測的答案
            if middle ** 2 > x:  # 猜的數字平方大於 x，猜大了
                right = middle - 1
            else:  # 猜的數字平方小於等於 x，猜的還不夠大
                left = middle + 1
        return right  # right 停在最後一個平方不超過 x 的數字，就是答案