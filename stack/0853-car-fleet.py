# 853 - Car Fleet
# https://leetcode.com/problems/car-fleet/
# Medium | Stack (Monotonic Stack)
# 思路: 先用 zip 把 position 和 speed 一次遍歷配對起來,
# 對每台車算出「如果沒有任何阻擋,自己單獨到達 target 所需的時間」:
# time = (target - position) / speed,存成 (position, time) 的 pair。
# 把 pairs 依照 position 由大到小排序(reverse=True),
# 這樣離 target 最近的車會排在最前面,優先被處理、優先形成確定的車隊。
# 用 stack 存目前已經確定車隊的到達時間。
# 逐一掃描排序後的 pairs:
# 如果 stack 是空的(第一台車,自己就是第一個車隊),或是這台車的 time
# 比 stack top(目前最新確定車隊)的 time 大(代表它比前面的車隊慢,追不上,
# 會自己形成一個新車隊),就把它的 time push 進 stack。
# 如果這台車的 time 小於等於 stack top,代表它會追上前面的車隊、合併成同一隊,
# 不需要做任何事(不 push,因為它不會形成新的獨立車隊)。
# 最後 stack 裡的元素個數,就是總共形成的車隊數量。
# Pattern 筆記: 這題的 pattern 是排序後搭配 monotonic stack,
# 下次看到「需要先排序才能決定誰會被誰吸收/追上」、
# 「用到達時間而非位置本身來判斷分組」這種特徵就用這個方法。
# Time: O(n log n),排序花費 O(n log n),掃描是 O(n) | Space: O(n)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        for p, s in zip(position, speed):
            time = (target - p) / s
            pairs.append((p, time))
        pairs = sorted(pairs, reverse=True)
        for pair in pairs:
            if not stack or pair[1] > stack[-1]:
                stack.append(pair[1])
        return len(stack)