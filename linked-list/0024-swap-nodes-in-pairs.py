# https://leetcode.com/problems/swap-nodes-in-pairs/
# Difficulty: Medium
# Type: Linked List, Dummy Node
#
# 思路:
# 1. 建立 dummy 接在 head 前面，prev 從 dummy 出發，cur 從 head 出發
# 2. 迴圈條件 cur and cur.next，確保還有一整對可以交換
# 3. 每一圈 node1 = cur、node2 = cur.next，先用 tmp 存下一對的開頭 cur.next.next
# 4. 改三條線：prev.next = node2、node2.next = node1、node1.next = tmp
# 5. prev 移到 node1（交換後的這對尾巴），cur 移到 tmp（下一對開頭）
# 6. 最後 return dummy.next
#
# Pattern 筆記: 這題的 pattern 是 dummy node + 指標重新接線，下次看到串列要成對或分段調整節點、head 可能會改變的特徵就用這個方法。
#
# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # dummy 接在 head 前面，因為交換後 head 會改變
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head

        # 還有一整對才交換
        while cur and cur.next:
            node1 = cur
            node2 = cur.next
            # 先存下一對的開頭，避免改線後找不到
            tmp = cur.next.next

            # 交換：prev -> node2 -> node1 -> tmp
            prev.next = node2
            node2.next = node1
            node1.next = tmp

            # prev 移到這對的尾巴，cur 移到下一對開頭
            prev = node1
            cur = tmp

        return dummy.next