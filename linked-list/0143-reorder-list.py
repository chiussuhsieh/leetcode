# 0143. Reorder List
# https://leetcode.com/problems/reorder-list/
# 難度：Medium
# 類型：Linked List

# 思路：
# 目標是把 L0->L1->...->Ln 重排成 L0->Ln->L1->Ln-1->...，可以拆解成三個已學過的
# 技巧組合：找中點 + 反轉 + 交錯合併。
#
# Step 1（找中點）：用快慢指標，fast 每次走 2 步、slow 每次走 1 步，都從 head
# 出發，直到 fast 走到底（while fast and fast.next）。slow 最後停在前半段的
# 最後一個節點（奇數個節點時前半段比後半段多一個，例如 5 個節點時前半 3 個、
# 後半 2 個）。用 newHead = slow.next 保存後半段起點，再用 slow.next = None
# 把前後兩段徹底斷開，變成兩個獨立串列。
#
# Step 2（反轉後半段）：對 newHead 開頭的後半段做標準的三指標反轉
# （prev、cur、temp），邏輯跟 Reverse Linked List 完全相同，反轉後 prev 即為
# 新的起點（例如 4->5 變成 5->4）。
#
# Step 3（交錯合併）：pointer1 指向前半段起點、pointer2 指向反轉後的後半段起點，
# 每輪都用 tmp 暫存 pointer1 原本的下一個節點（避免斷鏈後迷路，跟 Reverse
# Linked List 的技巧同源），依序接上 pointer2、pointer1 往前推進；pointer2
# 這邊同理也用 tmp2 暫存後移動。
# 迴圈條件用 while pointer2（而不是 pointer1 or pointer2），因為前半段本來就
# 比後半段多一個節點，多出來的最後一個節點在斷開時 next 已經是 None，
# 自然留在結尾，不需要額外處理；用 pointer2 是否耗盡來判斷合併是否結束最安全。

# Pattern 筆記：
# 這題是這一組（dummy node / 合併類）的綜合題，把「快慢指標找中點」
# （源自 Linked List Cycle）、「三指標反轉」（源自 Reverse Linked List）、
# 「雙指標交錯合併」（源自 Merge Two Sorted Lists 的合併概念）三個獨立技巧
# 組裝成一題。之後遇到看起來複雜的 linked list 題目，可以先想「這題是不是能
# 拆解成幾個已經會的子技巧」，而不是從零想新解法。
# 合併階段務必用 tmp 暫存下一步要走的節點，這是貫穿整個 linked list 章節的
# 共同陷阱：只要會修改 .next，就一定要先暫存原本的 .next，否則斷鏈後找不回路。

# Time complexity: O(n)，三個步驟各自線性走訪一遍
# Space complexity: O(1)，只用固定數量的指標變數

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Step 1: 快慢指標找中點，slow 停在前半段最後一個節點
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        newHead = slow.next  # 後半段起點
        slow.next = None     # 切斷前後兩段

        # Step 2: 反轉後半段（標準三指標反轉）
        cur = newHead
        prev = None
        while cur:
            temp = cur.next   # 暫存原本的下一個，避免斷鏈迷路
            cur.next = prev
            prev = cur
            cur = temp
        secondHead = prev  # 反轉後的後半段起點

        # Step 3: 交錯合併前半段與反轉後的後半段
        pointer1 = head
        pointer2 = secondHead
        while pointer2:
            tmp = pointer1.next    # 暫存 pointer1 原本的下一個
            pointer1.next = pointer2
            pointer1 = tmp
            tmp2 = pointer2.next   # 暫存 pointer2 原本的下一個
            pointer2.next = pointer1
            pointer2 = tmp2