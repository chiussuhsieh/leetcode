# 739 - Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
# Medium | Stack (Monotonic Stack)
# 思路: 用 stack 存 (溫度, index) 的 pair,代表「還在等待未來更高溫度」的那些天。
# 逐一掃描 temperatures,對於每一天 i:
# 先用 while 迴圈檢查:只要 stack 不是空的、且今天溫度比 stack top 的溫度高,
# 就代表 stack top 那一天等到更高溫度了,把 (i - stack top 的 index) 填進 ans,
# 並把 stack top pop 掉,繼續用同一個 while 迴圈檢查新的 stack top
# (因為今天可能同時解決好幾天的等待,例如溫度突然大幅上升)。
# while 迴圈結束後(代表今天無法再解決更多等待中的日子,或 stack 已經空了),
# 把今天 (temperatures[i], i) push 進 stack,讓它加入「等待未來更高溫度」的行列。
# 最後 ans 裡沒被更新到的日子維持初始值 0,代表沒有更高溫度的未來。
# Pattern 筆記: 這題的 pattern 是 monotonic stack(單調堆疊)入門題,
# stack 由底到頂維持遞減順序,下次看到「找下一個更大/更小元素」、
# 「需要往前找最近符合條件的元素」這種特徵就用這個方法。
# Time: O(n),每個元素最多被 push、pop 各一次,均攤 O(n) | Space: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                res = i - stack[-1][1]
                ans[stack[-1][1]] = res
                stack.pop()
            stack.append((temperatures[i], i))
        return ans