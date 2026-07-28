# 901 - Online Stock Span
# https://leetcode.com/problems/online-stock-span/
# Medium | Stack (Monotonic Stack)
# 思路: 用 stack 存 (price, span) 的 pair,由底到頂價格維持遞減,
# 代表「目前為止還沒被更高(或相等)價格吞併的那些天,以及它們各自累積的 span」。
# 每次呼叫 next(price) 時:
# 先把這次的 span 初始化成 1(至少包含今天自己)。
# 用 while 迴圈,只要 stack 不是空的、且今天的 price 大於等於 stack top 的價格,
# 就代表今天可以吞併 stack top 那一層(以及它已經累積的天數):
# 把 stack top 的 span 累加進今天的 span,再把 stack top pop 掉,
# 繼續用同一個 while 迴圈檢查新的 stack top,
# 因為可能有連續好幾層都符合吞併條件,不是只有最上面那一層(所以不能只做一次 if)。
# 迴圈結束後(遇到比今天價格還高的層,或 stack 已經空了),
# 把 (price, span) push 進 stack,並回傳 span。
# span 用 local 變數即可,不需要是 instance attribute,
# 因為它只在這一次 next() 呼叫內有意義,不需要跨越多次呼叫存活;
# stack 則必須是 self.stack,因為它要在多次 next() 呼叫之間持續累積保留。
# Pattern 筆記: 這題的 pattern 是 monotonic stack 搭配「累加附加資訊」,
# 下次看到「即時串流資料,且答案需要吞併/濃縮前面連續符合條件的區間」這種特徵就用這個方法。
# Time: next() 均攤 O(1),每個元素最多被 push、pop 各一次 | Space: O(n)

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span