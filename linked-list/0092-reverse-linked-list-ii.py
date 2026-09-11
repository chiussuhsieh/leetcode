# 0092. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/
# 難度：Medium
# 類型：Linked List

# 思路：
# 只反轉 [left, right] 這段區間，其餘部分不動。因為反轉範圍可能包含 head 本身
# （left=1），用 dummy node 讓「反轉範圍是否包含 head」都能用同一套邏輯處理。
#
# 定位：prevNode 從 dummy 出發走 (left-1) 步，停在反轉區間前一個節點；
# rightNode 從 dummy 出發走 right 步，停在反轉區間的最後一個節點。
# 兩個變數必須另外命名，不能覆蓋參數 left、right 本身（一旦覆蓋，range() 就無法
# 使用原本的整數值）。
#
# 斷開：先用 tmp2 存下 rightNode.next（反轉區間後面那一段的起點，因為斷開後
# 就再也找不到它），再用 newHead 存下 prevNode.next（反轉區間的第一個節點，
# 因為斷開後也會找不到它）。接著 prevNode.next = None、rightNode.next = None，
# 把 [left, right] 這段變成一個完全獨立、範圍固定的小串列。
#
# 反轉：對這個獨立小串列套用標準三指標反轉（prev、cur、temp），因為已經斷開，
# 用一般的 while cur 就能反轉到底，不會誤傷區間外的節點。
#
# 接回去：反轉迴圈跑完後，prv 是反轉後的新起點（原本的 rightNode），
# newHead（原本反轉區間的第一個節點）變成反轉後的新尾巴。
# tmp1（即 prevNode）接到 prv，newHead 接到 tmp2，完成拼接。
# 最後回傳 dummy.next 而非 head，因為 left=1 時原本的 head 會被移到區間尾端，
# 不再是新的起點。

# Pattern 筆記：
# 這題是 Reverse Linked List 的「區間版」，核心策略是「先斷開成獨立小串列，
# 再套用已經熟悉的標準反轉，最後把兩端接回去」，而不是在反轉迴圈裡去特判邊界。
# 這個「斷開、處理、接回去」的模式，跟 Reorder List 拆成三段獨立子問題的思路
# 是同一種工程手法：把複雜題目拆解成「定位」「斷開」「處理」「重新連接」四個
# 獨立、各自簡單的步驟，逐一驗證，避免所有邏輯擠在一個迴圈裡容易出錯。
# dummy node 再次用於處理「操作範圍可能包含 head」的邊界情況。

# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prevNode = dummy   # 反轉區間前一個節點
        rightNode = dummy  # 反轉區間的最後一個節點
        for i in range(left - 1):
            prevNode = prevNode.next
        for i in range(right):
            rightNode = rightNode.next

        tmp1 = prevNode           # 反轉區間前一個節點（之後接反轉後的新起點）
        tmp2 = rightNode.next     # 反轉區間後面那一段的起點（先存，斷開後才找得到）
        newHead = prevNode.next   # 反轉區間的第一個節點（先存，斷開後才找得到）
        prevNode.next = None      # 斷開前面
        rightNode.next = None     # 斷開後面，[left, right] 變成獨立小串列

        # 標準三指標反轉這個獨立小串列
        cur = newHead
        prv = None
        while cur:
            tmp = cur.next
            cur.next = prv
            prv = cur
            cur = tmp

        tmp1.next = prv        # prv 是反轉後的新起點，接到前一段
        newHead.next = tmp2    # newHead 是反轉後的新尾巴，接到後一段
        return dummy.next      # 用 dummy.next 而非 head，避免 left=1 時 head 已不是起點