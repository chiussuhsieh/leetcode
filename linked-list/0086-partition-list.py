# https://leetcode.com/problems/partition-list/
# Difficulty: Medium
# Type: Linked List, Dummy Node, Two Lists
#
# 思路:
# 1. 建立兩個 dummy：dummyLess 放 < x 的節點，dummyGreat 放 >= x 的節點
# 2. pointer1 從 dummyLess 出發、pointer2 從 dummyGreat 出發，各自當作兩條串列的尾巴
# 3. cur 從 head 走過原串列，cur.val < x 就接到 pointer1 後面並移動 pointer1，否則接到 pointer2 後面並移動 pointer2
# 4. 每圈結束 cur = cur.next，因為只改了尾巴的 .next，cur 自己的 .next 沒被改，所以不用另外存
# 5. 迴圈結束後 pointer2.next = None 切掉大串列尾巴原本的線，避免形成環
# 6. pointer1.next = dummyGreat.next 把小串列接上大串列，return dummyLess.next
#
# Pattern 筆記: 這題的 pattern 是兩個 dummy 分別收集再接起來，下次看到串列要依條件分組、又要保留原本相對順序的特徵就用這個方法。
#
# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        # 兩條串列各自的 dummy
        dummyGreat = ListNode()
        dummyLess = ListNode()
        cur = head
        # 兩條串列各自的尾巴指標
        pointer1 = dummyLess
        pointer2 = dummyGreat

        while cur:
            if cur.val < x:
                # 接到小串列尾巴，尾巴往後移
                pointer1.next = cur
                pointer1 = pointer1.next
            else:
                # 接到大串列尾巴，尾巴往後移
                pointer2.next = cur
                pointer2 = pointer2.next
            # 只改了尾巴的 .next，cur.next 還在
            cur = cur.next

        # 切掉大串列尾巴原本指向的節點，避免形成環
        pointer2.next = None
        # 小串列接上大串列
        pointer1.next = dummyGreat.next
        return dummyLess.next