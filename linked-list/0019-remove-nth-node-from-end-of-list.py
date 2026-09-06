# 0019. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# 難度：Medium
# 類型：Linked List

# 思路：
# Two-pass 解法：第一遍走訪整個串列算出長度 length，倒數第 n 個節點就是正數第
# (length - n + 1) 個。第二遍從 dummy 出發，走 (length - n + 1 - 1) 步，
# 停在「要移除節點的前一個」，再把它的 next 指向下下個節點（跳過要移除的節點）。
# 用 dummy node 是因為要移除的節點可能剛好是 head 本身，dummy 讓這種情況跟一般
# 情況共用同一套邏輯，不需要特殊判斷。
#
# One-pass 優化：用 fast、slow 兩個指標，都從 dummy 出發，維持固定距離 n。
# 先讓 fast 領先走 n 步，之後 fast、slow 同步前進（各走一步），直到 fast.next
# 是 None（fast 停在最後一個節點，不是走到 None）。
# 因為 fast 領先 slow 固定 n 步，當 fast 走到最後一個節點時，slow 剛好停在
# 倒數第 n 個節點的前一個，這正是要移除節點的前一個。
# 終止條件用 fast.next is None 而不是 fast is None，是為了讓 slow 精準停在
# 「前一個」而不是「要移除的節點本身」，這樣才能用同一行 slow.next = slow.next.next
# 完成移除，不用額外判斷。
#
# Two-pass 與 one-pass 的漸進時間複雜度相同（都是 O(n)），差別只在常數項
# （two-pass 走兩趟、one-pass 走一趟），面試常見考法是先給 brute force 再問
# 能否一次通過來考察 two-pointer 固定距離技巧。

# Pattern 筆記：
# 這是「固定距離雙指標」的 pattern：兩個指標維持固定距離 n，前面的指標走到底時，
# 後面的指標自然停在「倒數第 n 個」的位置。跟 Linked List Cycle 的快慢指標
# （距離會動態變化）是不同的變形，這裡距離是固定的。
# dummy node 技巧再次用來處理「操作對象可能是 head 本身」的邊界情況，
# 這個技巧會持續出現在後面 Reorder List、Reverse Linked List II 等題目。

# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()  # 哨兵節點，處理移除的剛好是 head 的邊界情況
        dummy.next = head
        fast = dummy
        slow = dummy
        for i in range(n):     # fast 先領先 slow n 步
            fast = fast.next
        while fast.next:       # fast 停在最後一個節點（不是走到 None）
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next  # slow 停在要移除節點的前一個，跳過它
        return dummy.next