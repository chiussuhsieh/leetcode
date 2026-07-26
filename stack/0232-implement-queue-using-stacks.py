# 232 - Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/
# Easy | Stack
# 思路: 用兩個 stack,一個是 stack(負責接收 push 進來的元素),
# 一個是 tempStack(負責倒出去給 pop/peek 用)。
# push(x) 的時候,單純把 x append 進 stack,不做任何搬移。
# pop() 和 peek() 的時候,先檢查 tempStack 是否為空:
# 如果 tempStack 是空的,才把 stack 裡的元素一個一個 pop 出來、
# 依序 append 進 tempStack(這樣順序就會反過來,最早進去的元素會跑到 tempStack 頂部)。
# 如果 tempStack 已經有元素(代表還有元素還沒處理完),就不用再搬,直接對 tempStack 操作,
# 避免打亂原本 tempStack 裡的順序。
# pop() 從 tempStack pop 出頂部元素並回傳。
# peek() 只看 tempStack 頂部元素(用 [-1]),不移除。
# empty() 要 stack 和 tempStack 都是空的,才代表 queue 真的是空的。
# Pattern 筆記: 這題的 pattern 是用「兩個 stack,一個負責接收、一個延遲搬移」來模擬 queue 的 FIFO 行為,
# 下次看到「只能單端操作的資料結構,要模擬另一種順序的資料結構」這種特徵就用這個方法。
# Time: push 是 O(1);pop / peek 均攤下來是 O(1)(每個元素一輩子只會被搬移一次) | Space: O(n)

class MyQueue:

    def __init__(self):
        self.stack = []
        self.tempStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.tempStack:
            while self.stack:
                element = self.stack.pop()
                self.tempStack.append(element)
        popElement = self.tempStack.pop()
        return popElement

    def peek(self) -> int:
        if not self.tempStack:
            while self.stack:
                element = self.stack.pop()
                self.tempStack.append(element)
        return self.tempStack[-1]

    def empty(self) -> bool:
        if not self.tempStack and not self.stack:
            return True
        return False