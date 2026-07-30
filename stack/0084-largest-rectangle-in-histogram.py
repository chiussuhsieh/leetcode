# 84 - Largest Rectangle In Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Hard | Stack (Monotonic Stack)
# 思路: 用 stack 存 (start_index, height) 的 pair,start_index 代表這個高度
# 往左最遠可以延伸到的起始位置,stack 由底到頂維持高度遞增。
# 逐一掃描 heights,對於每一根新柱子 (i, h):
# start 先設成 i 自己。
# 用 while 迴圈檢查:只要 stack 不是空的、且 stack top 的高度大於 h,
# 代表 stack top 那根柱子(以自己高度為準的矩形)不能再往右延伸了
# (因為新柱子比較矮,撐不住 stack top 那個高度),所以要 pop 出來結算面積:
# 寬度 = i - index(被 pop 那個的 start_index),面積 = height * 寬度,更新 maxArea。
# 並把 start 更新成被 pop 掉那個的 index(繼承左邊界,因為新柱子雖然比較矮,
# 但它的「勢力範圍」可以往左延伸到被吞併那些柱子的起點)。
# 這個 while 迴圈會連續 pop,直到 stack top 不再比新柱子高,或 stack 空了為止,
# 才把 (start, h) push 進 stack。
# 迴圈跑完整個 heights 之後,stack 裡可能還剩下一些柱子——這些柱子右邊沒有
# 遇到比它們矮的,代表可以一路延伸到陣列最右邊。這時候要把 stack 清空,
# 這次「右邊界」固定用 len(heights)(因為迴圈已經跑完,沒有新的 i 可以用),
# 依序 pop 出來計算面積並更新 maxArea。
# 最後回傳 maxArea。
# Pattern 筆記: 這題的 pattern 是 monotonic stack 集大成應用,同時追蹤
# 左邊界(繼承被吞併柱子的起點)和右邊界(觸發 pop 的當下 index),
# 且結尾需要額外清空 stack(或在陣列尾端補一個高度 0 的哨兵值達到同樣效果),
# 下次看到「找出以每個元素為基準,能往左右延伸的最大範圍」這種特徵就用這個方法。
# Time: O(n),每個元素最多被 push、pop 各一次,均攤 O(n) | Space: O(n)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (start_index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea