# 846. Hand of Straights
# https://leetcode.com/problems/hand-of-straights/
# 難度：Medium
# 類型：Greedy

# 思路：
# 1. 如果 len(hand) % groupSize != 0，直接回傳 False
# 2. 用 Counter 記錄每張牌的數量
# 3. 從最小的牌開始，每次嘗試建立一個 groupSize 的連續 group
# 4. 如果某張牌不夠用，回傳 False

# Time: O(n log n)，sorting
# Space: O(n)

from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False               # 牌的總數不能被 groupSize 整除，直接 False

        count = Counter(hand)          # 記錄每張牌的數量

        for card in sorted(count):     # 從最小的牌開始（sort key）
            while count[card] > 0:     # 這張牌還有剩，嘗試建立一個 group
                for i in range(groupSize):
                    count[card + i] -= 1    # 用掉連續的牌
                    if count[card + i] < 0:
                        return False        # 某張牌不夠用，無法建立 group

        return True                    # 所有牌都成功分組