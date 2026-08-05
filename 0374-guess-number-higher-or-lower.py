# 0374. Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/
# 難度：Easy
# 類型：Binary Search

# 思路：
# 用 binary search 樣板，left 從 1 開始，right 是 n。
# 用 while left <= right 持續搜尋，middle 取中間值。
# 呼叫 guess(middle) 拿到系統回傳的結果，存到 target 這個變數（只呼叫一次，避免重複呼叫 API）。
# 如果 target 是 0，代表猜中了，直接回傳 middle。
# 如果 target 是 -1，代表猜的數字比 pick 大，right 移到 middle - 1。
# 否則代表猜的數字比 pick 小，left 移到 middle + 1。

# Pattern 筆記：
# 這題的 pattern 是 binary search 樣板包一層外部 API，下次看到「用回傳訊號判斷方向、且該訊號來自外部函式」的特徵就用這個方法，並記得把 API 結果存到變數避免重複呼叫。

# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1  # 搜尋範圍的左邊界
        right = n  # 搜尋範圍的右邊界
        while left <= right:  # 左右邊界還沒交叉就繼續找
            middle = (left + right) // 2  # 取中間值
            target = guess(middle)  # 呼叫 API，結果存到變數，避免重複呼叫
            if target == 0:  # 猜中了
                return middle
            elif target == -1:  # 猜的數字比 pick 大
                right = middle - 1
            else:  # 猜的數字比 pick 小
                left = middle + 1