# 84 - Largest Rectangle In Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Hard | Stack (Monotonic Stack)
# 思路：
# stack 存 (start_index, height)，其中 start_index 表示這個高度最早可以開始的位置。
# 從左到右掃描每根柱子：
# 1. 先假設這根柱子的起點就是自己，所以 start = i。
# 2. 如果目前柱子比 stack 最上面的柱子矮，
#    代表 stack 最上面的柱子已經不能再往右延伸了，
#    因為遇到了一根更矮的柱子。
#
# 3. 因此把它 pop 出來，計算它的最大面積：
#       高 = 被 pop 的 height
#       寬 = i - start_index
#       面積 = height × width
#    更新 maxArea。
# 4. 被 pop 的柱子原本可以延伸到更左邊，
#    而現在這根較矮的柱子其實也可以覆蓋那一段，
#    所以把 start 更新成被 pop 的 start_index，
#    讓新的柱子繼承它的左邊界。
# 5. 持續 pop，直到 stack 為空，
#    或 stack 最上面的高度 <= 目前柱子高度，
#    再把 (start, h) 放進 stack。
#
# 掃描完成後，stack 裡剩下的柱子代表：
# 它們一路都沒有遇到更矮的柱子，
# 所以可以一直延伸到陣列最後。
#
# 因此再把 stack 中每根柱子的面積補算一次：
#    高 = height
#    寬 = len(heights) - start_index
# 更新 maxArea。
#
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