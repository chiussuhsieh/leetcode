# 0622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/
# 難度：Medium
# 類型：Linked List（Design，陣列模擬環狀結構）

# 思路：
# 一般用固定陣列實作佇列，front 往後移動後，前面空出來的位置無法重複利用，
# 會浪費空間。Circular（環狀）的概念是讓 index 走到陣列尾端後自動繞回開頭，
# 用餘數運算 % capacity 達成，把陣列想像成首尾相接的圓圈。
#
# 判斷「空」與「滿」是環狀佇列設計的核心難點：如果只靠 front == rear 這個
# 條件，佇列全空跟佇列全滿時可能會撞到同一種狀態，無法區分。解法是額外用
# self.count 記錄目前元素個數，這樣就不需要維護 rear 這個變數——
# 「尾端 index」可以直接用 (front + count - 1) % capacity 算出來，
# 「新元素該放的位置」則是 (front + count) % capacity。
#
# enQueue：檢查 count >= capacity 判斷滿了沒；沒滿的話用上述公式算出位置、
# 寫入陣列、count += 1。
# deQueue：檢查 count == 0 判斷空了沒；不是空的話直接把 front 往前移一格
# （用 (front + 1) % capacity 處理繞圈），count -= 1。不需要真的把陣列裡
# 的值清空或改成 0，因為所有讀取操作（enQueue 算新位置、Front、Rear）都是
# 用 front/count 算出合法 index，範圍外的殘留值永遠不會被讀到，資料結構的
# 有效性完全由 front 和 count 定義，不依賴陣列內容本身。
# Front / Rear：分別讀取 queue[front] 和 queue[(front+count-1)%capacity]，
# 若 count == 0 則回傳 -1。
# isEmpty / isFull：直接回傳 count == 0 / count >= capacity 這兩個布林
# 表達式本身，不需要額外包一層 if-else。

# Pattern 筆記：
# 這是「用固定陣列模擬環狀結構」的 pattern，核心技巧是 index 運算全部套用
# % capacity 讓位置在 0 到 capacity-1 之間循環。用一個計數變數（而非額外
# 維護 rear 指標，或犧牲一格空間）來區分空/滿狀態，是這類設計題常見的
# 兩種標準解法之一，選哪種看個人偏好，用計數變數通常更直覺、不容易在邊界
# 條件出錯。這個 pattern 之後在 LRU Cache、LFU Cache 這類 design 題裡，
# 「用簡單變數取代額外的指標維護」的思路會反覆出現。

# Time complexity: 所有操作皆為 O(1)，因為位置都用數學運算直接算出，不需走訪陣列
# Space complexity: O(k)，k 為佇列容量，陣列大小固定

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k   # 固定大小陣列，佔位值不影響邏輯
        self.front = 0          # 開頭元素的 index
        self.count = 0          # 目前元素個數，用來判斷空/滿，取代額外的 rear 指標
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.count >= self.capacity:
            return False
        place = (self.front + self.count) % self.capacity  # 新元素該放的位置
        self.queue[place] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.front = (self.front + 1) % self.capacity  # front 往前移一格，繞圈處理
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        place = (self.front + self.count - 1) % self.capacity  # 尾端元素的 index
        return self.queue[place]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count >= self.capacity