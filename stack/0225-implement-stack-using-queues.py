# 225 - Implement Stack Using Queues
# https://leetcode.com/problems/implement-stack-using-queues/
# Easy | Stack
# 思路: 用 deque 當作底層的 queue。
# push(x) 的時候,先把 x 加到 queue 尾巴,
# 接著重複 (queue 長度 - 1) 次:把 queue 最前面的元素 popleft 出來,
# 再 append 回 queue 尾巴,這樣可以讓 x 轉到 queue 最前面,
# 同時保持其他元素原本的相對順序不變。
# 這樣設計之後,queue 最前面(index 0)永遠是最後一個被 push 進去的元素,
# 也就是 stack 的 top。
# pop() 直接 popleft 拿出最前面的元素(就是 stack top)。
# top() 直接回傳 queue[0]。
# empty() 檢查 queue 是否為空。
# Pattern 筆記: 這題的 pattern 是用「push 時重新排列 queue 順序」來模擬 stack 的 LIFO 行為,
# 下次看到「用一種資料結構的操作去模擬另一種資料結構」這種特徵就用這個方法。
# Time: push 是 O(n),pop / top / empty 都是 O(1) | Space: O(n)

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            element = self.queue.popleft()
            self.queue.append(element)

    def pop(self) -> int:
        popElement = self.queue.popleft()
        return popElement

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if not self.queue:
            return True
        else:
            return False