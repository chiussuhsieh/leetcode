# 0875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/
# 難度：Medium
# 類型：Binary Search

# 思路：
# 這題要找的答案不是陣列裡的某個值，而是「吃香蕉的速度 k」這個數值本身，
# 在「答案空間」上做 binary search（速度的可能範圍是 1 到 max(piles)）。
# left 設 1，right 設 max(piles)，用 while left < right 持續搜尋。
# 每一輪先把 totalHours 歸零，middle 取中間值當作這一輪猜測的速度。
# 用內層 for 迴圈算出：如果用這個速度 middle 吃，吃完每一堆各別需要幾小時（有餘數就要多花一小時），
# 把每一堆的時數加總成 totalHours。
# 如果 totalHours > h，代表這個速度太慢，吃不完，left 移到 middle + 1（往更快的方向找）；
# 否則代表這個速度夠快（甚至可能太快了，但沒關係，只要不超過 h 都算合格候選），
# right 移到 middle（不 -1，因為 middle 本身有可能就是最小合格速度，不能排除）。
# 迴圈結束時 left == right，就是最小的合格速度。

# Pattern 筆記：
# 這題的 pattern 是 binary search on answer space（在答案的可能範圍上搜尋，而非陣列本身），
# 下次看到「要找一個滿足條件的最小/最大數值、且這個數值具有單調性（速度越快耗時越短）」的特徵就用這個方法。
# 跟 0069 Sqrt(x) 一樣是在答案空間搜尋，但這題要找「最小合格值」，用 right = middle 保留候選、
# while left < right 收斂到 left == right。

# Time complexity: O(n log m)，n 為 piles 長度，m 為 max(piles)
# Space complexity: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1  # 速度的最小可能值
        right = max(piles)  # 速度的最大可能值
        while left < right:  # 左右邊界還沒相遇就繼續找
            totalHours = 0  # 每一輪重新計算總時數
            middle = (left + right) // 2  # 這一輪猜測的速度
            for pile in piles:  # 計算用這個速度吃完每一堆各別需要幾小時
                if pile % middle:  # 有餘數，要多花一小時吃完剩下的
                    time = (pile // middle) + 1
                else:  # 剛好整除
                    time = pile // middle
                totalHours += time
            if totalHours > h:  # 這個速度太慢，吃不完
                left = middle + 1
            else:  # 這個速度夠快，是合格候選（保留 middle）
                right = middle
        return left  # left 和 right 相遇的位置就是最小合格速度