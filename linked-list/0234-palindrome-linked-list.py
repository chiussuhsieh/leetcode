# https://leetcode.com/problems/palindrome-linked-list/
# Difficulty: Easy
# Type: Linked List, Fast & Slow Pointers
#
# 思路:
# 1. fast 從 head.next 出發、slow 從 head 出發，fast 一次走兩步、slow 一次走一步
#    迴圈結束時 slow 停在前半的最後一個節點（奇數時中間節點歸前半）
# 2. second = slow.next 當作後半的開頭，再用 slow.next = None 把前後半斷開
# 3. 用 prev / cur / tmp 原地反轉後半，反轉完 prev 就是後半的新開頭
# 4. new 從反轉後半出發、cur 從 head 出發，逐一比較 val
#    用 while new 當停止條件，因為後半長度 <= 前半
# 5. 有任何一對不同就 return False，全部比完 return True
#
# Pattern 筆記: 這題的 pattern 是快慢指針找中點 + 反轉後半，下次看到串列要對稱比對、又要求 O(1) 空間的特徵就用這個方法。
#
# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        # fast 領先一步，讓偶數長度時 slow 停在前半最後一個
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 斷開前半和後半
        second = slow.next
        slow.next = None

        # 原地反轉後半
        cur = second
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # 前半和反轉後的後半逐一比較
        new = prev
        cur = head
        while new:
            if new.val != cur.val:
                return False
            new = new.next
            cur = cur.next
        return True