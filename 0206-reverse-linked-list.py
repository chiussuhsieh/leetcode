# 0206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# 難度：Easy
# 類型：Linked List

# 思路：
# 要把 1 -> 2 -> 3 -> None 反轉成 3 -> 2 -> 1 -> None，關鍵在於：
# 反轉後，每個節點的 next 要指向它「反轉前的前一個節點」。
# 但走訪時如果直接把 cur.next 改掉，會弄丟原本指向的下一個節點，導致後面走不下去。
#
# 解法：用三個變數 prev、cur、temp 邊走邊翻轉。
# 每一輪：先用 temp 暫存 cur.next（保留原本的路，避免弄丟後半段）；
# 再把 cur.next 指向 prev（完成這個節點的反轉）；
# 然後 prev、cur 各自往前推進一格（prev = cur, cur = temp）。
# 迴圈跑到 cur 為 None 時結束，此時 prev 就是新的 head（反轉後的第一個節點）。
#
# prev 初始化為 None，因為原本 head 反轉後會變成新的 tail，它的 next 應該指向 None。

# Pattern 筆記：
# 這是 linked list 反轉的基本 pattern，核心是「三指標推進」：
# prev（已反轉部分的頭）、cur（目前處理的節點）、temp（暫存原本的 next，避免斷鏈後迷失方向）。
# 之後遇到 Reverse Linked List II（反轉區間）、Reverse Nodes in K Group（分段反轉），
# 都是這個 pattern 的延伸應用，差別只在於反轉的起訖點怎麼定位、反轉完怎麼接回原鏈。
# Iterative 解法空間複雜度 O(1)；若用 recursive 解法，call stack 深度為 O(n)，
# 空間複雜度會變成 O(n)，這是面試常見追問點。

# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # 已反轉部分的頭，初始為 None（原 head 反轉後會變 tail）
        cur = head   # 目前正在處理的節點
        while cur:
            temp = cur.next   # 暫存原本的下一個節點，避免斷鏈後迷失方向
            cur.next = prev   # 把目前節點的 next 指向前一個節點，完成反轉
            prev = cur        # prev 往前推進一格
            cur = temp        # cur 往前推進一格
        return prev  # cur 變 None 時，prev 就是反轉後的新 head