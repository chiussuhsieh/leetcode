# 155 - Min Stack
# https://leetcode.com/problems/min-stack/
# Medium | Stack
# 思路: 用兩個 stack 同步維護:stack 存正常的元素,minStack 逐一對應記錄
# 「當 stack 只有到這個 index 為止的元素時,當時的最小值是多少」。
# push(value) 的時候,stack 正常 append value;
# minStack 則 append「value 跟 minStack 目前 top(如果 minStack 是空的就用 value 本身)兩者中較小的那個」,
# 這樣 minStack 的 top 永遠是目前為止看過的最小值。
# pop() 的時候,stack 和 minStack 同步各自 pop 一次,
# 這樣可以維持兩個 stack 長度與對應關係一致,讓 minStack 的 top 自動回復到正確的歷史最小值,
# 不需要重新計算。
# top() 只看 stack 的 top(用 [-1]),不移除。
# getMin() 只看 minStack 的 top(用 [-1]),不移除,直接 O(1) 拿到目前最小值。
# Pattern 筆記: 這題的 pattern 是用「輔助 stack 同步紀錄額外狀態」來讓查詢操作變成 O(1),
# 下次看到「stack 操作中需要同時查詢某個統計值(最小值/最大值/總和等)」這種特徵就用這個方法。
# Time: push / pop / top / getMin 皆為 O(1) | Space: O(n)

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.minStack.append(min(value, self.minStack[-1] if self.minStack else value))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        element = self.stack[-1]
        return element

    def getMin(self) -> int:
        element = self.minStack[-1]
        return element