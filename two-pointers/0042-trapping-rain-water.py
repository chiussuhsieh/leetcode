# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# 難度：Hard
# 類型：Two Pointers

# 思路：
# 某個位置能積多少水，取決於「左邊最高的柱子」和「右邊最高的柱子」中較矮的那個，
# 再減去該位置本身的高度。
# 用 left、right 兩個指標從兩端往中間收斂，同時維護 left_max、right_max
# （分別代表「left 走過的路徑上看過的最高柱子」和「right 走過的路徑上看過的最高柱子」）。
# 關鍵觀察：如果 left_max <= right_max，代表左右兩邊較矮的那個「一定是 left_max」，
# 這件事已經確定、不會再改變（因為 right_max 之後只會更大或不變），
# 所以可以放心計算 left 這個位置的積水量，不需要等右邊完全掃完。
# 每一輪：
#   若 left_max <= right_max：先更新 left_max（包含 left 自己），
#     計算 water += left_max - height[left]，再移動 left。
#   否則：對稱處理 right 那一側。
# 迴圈條件用 left <= right（不是 left < right），因為兩指標相遇的那一格，
# 還沒被任何一次迭代處理過，需要讓它被算到最後一次。

# Pattern 筆記：
# 這題的 pattern 是「雙指標收斂 + 動態維護左右最大值（two pointers with running max）」，
# 下次看到「某個位置的結果取決於左右兩側最大值中較小的那個」且「不想對每個位置重新掃描左右兩邊」
# 的特徵，就用這個方法：從兩端往中間收斂，每次處理「較小 max 的那一側」，
# 因為那一側的較小值已經確定不會再變。

# Time: O(n)
# Space: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left <= right:
            if left_max <= right_max:
                # 左邊較矮（或相等），可以確定地計算 left 這一側的積水量
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                # 右邊較矮，對稱處理 right 這一側
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1

        return water