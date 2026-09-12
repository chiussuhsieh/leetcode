# 0138. Copy List With Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/
# 難度：Medium
# 類型：Linked List

# 思路：
# 每個節點除了 next 還有 random（可指向任意節點或 None），深拷貝的困難點在於：
# 如果邊走訪邊建立新節點、邊設定 random，當走到節點 A 要設 random 時，
# A.random 指向的節點可能還沒被複製過（因為 random 可以指向任意位置，
# 包括還沒走到的後面節點）。
#
# 解法用 hashmap 建立「原節點 → 新節點」的對應關係，分兩輪走訪解決順序問題：
#
# 第一輪：只做「複製每個節點的 val，建立對應關係」這件事，不處理 next 和
# random。走訪原串列，對每個節點建立新節點 Node(cur.val)，存進
# oldToNew[cur] = 新節點。用節點物件本身當 dict 的 key 是合法的，因為
# Python 自訂物件預設用身分（identity）做 hash，不同節點即使 val 相同也是
# 不同的 key。oldToNew 預先放入 {None: None}，讓查詢 next 或 random 為
# None 的情況也能安全查到 None，不用額外判斷。
#
# 第二輪：因為第一輪已經幫「每一個」原節點都建好對應的新節點，所以這時候
# 不管 next 或 random 指向哪裡，一定能在 hashmap 裡查到對應的複製節點。
# 對每個原節點 cur：oldToNew[cur].next = oldToNew[cur.next]，
# oldToNew[cur].random = oldToNew[cur.random]。
#
# 最後回傳 oldToNew[head]，也就是原本 head 對應的複製節點。

# Pattern 筆記：
# 這是「hashmap 映射舊物件到新物件」的 pattern，核心是用兩輪走訪拆解
# 「建立所有節點」和「設定所有連接關係」這兩個步驟，避免處理連接關係時
# 遇到「目標還沒被建立」的順序問題。這個 pattern 廣泛用於圖的深拷貝
# （Clone Graph 也是同樣的技巧：先建節點、再建邊）。
# 用節點物件本身當 hashmap 的 key，是這題的關鍵前提，值得記住 Python
# 物件預設可雜湊、用身分比較這個底層行為。

# Time complexity: O(n)，兩輪各走訪一次（漸進複雜度仍是 O(n)）
# Space complexity: O(n)，hashmap 存了 n 個節點的對應關係

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None: None}  # 原節點 -> 新節點，預放 None 避免額外判斷

        # 第一輪：只複製 val，建立對應關係
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToNew[cur] = copy
            cur = cur.next

        # 第二輪：利用已建好的對應關係，設定 next 和 random
        cur = head
        while cur:
            oldToNew[cur].next = oldToNew[cur.next]
            oldToNew[cur].random = oldToNew[cur.random]
            cur = cur.next

        return oldToNew[head]