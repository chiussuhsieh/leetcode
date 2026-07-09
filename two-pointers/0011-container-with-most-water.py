# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# 難度：Medium
# 類型：Two Pointers

# 思路：
# left 指向最左邊的線，right 指向最右邊的線，這時候寬度最大。
# 面積 = 寬度（right - left）× 高度（取兩條線中較矮的那條，因為水會從較矮的那邊溢出）。
# 每一輪計算目前面積、更新最大值，然後移動「較矮」的那個指標：
# 因為如果移動較高的那條線，寬度變小，但高度上限還是被矮的那條卡住，面積只會變小或不變；
# 移動較矮的那條線，雖然寬度也會變小，但至少有機會遇到更高的線，讓面積有提升的可能。
# 兩個指標往中間收斂，直到相遇為止。

# Pattern 筆記：
# 這題的 pattern 是「貪心雙指標收斂（greedy two pointers）」，
# 下次看到「找兩個元素形成的區間，要最大化某個由『較小值 × 距離』決定的目標」的特徵，
# 就從最外側開始收斂，每次移動較不利的那一側。

# Time: O(n)
# Space: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxA = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            maxA = max(area, maxA)

            # 移動較矮的那個指標，才有機會遇到更高的線提升面積
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxA