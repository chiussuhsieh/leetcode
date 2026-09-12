# 0025. Reverse Nodes In K Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# 難度：Hard
# 類型：Linked List

# 思路：
# 每 k 個節點為一組反轉，不足 k 個的最後一組保持原樣。可以看成「重複套用
# Reverse Linked List II 的策略（斷開成獨立小串列 → 標準反轉 → 接回去）」，
# 差別在於每一組的起訖點不是用固定的 left/right 位置算出來，而是動態判斷。
#
# 用 dummy node 起手，groupPrev 代表「目前這一組前面那個節點」，初始為 dummy。
# 用 while True + break（而非用某個變數自然變成 None 來停止），因為 groupPrev
# 不會自然變成 None，迴圈的終止條件是「checkK 檢查失敗」。
#
# checkK(node, k) 檢查從 node 開始是否存在 k 個節點：用一個區域變數走 k 次，
# 每次先確認目前節點不是 None 才移動，若中途遇到 None 代表不足，回傳 False；
# 迴圈完整跑滿 k 次都沒中斷，回傳 True。傳入的 node 必須是「這一組的起點」
# （即 groupPrev.next），不是 groupPrev 本身。
#
# 每一輪：
# 1. tmp = groupPrev.next（這一組的起點）
# 2. 從 tmp 出發走 k-1 步找到 end（這一組的終點）
# 3. 用 tmp2 存下 end.next（後段起點，斷開後才找得到）
# 4. groupPrev.next = None、end.next = None，把這一組變成獨立小串列
# 5. 對這段獨立小串列做標準三指標反轉
# 6. 接回去：groupPrev.next = prev（反轉後新起點），tmp.next = tmp2（反轉後
#    新尾巴接到後段）
# 7. groupPrev = tmp（這一組反轉後的新尾巴，變成下一組的「前面那個節點」）
#
# 最後回傳 dummy.next。

# Pattern 筆記：
# 這題是翻轉家族的收尾，本質是「重複執行 Reverse Linked List II 的單組處理邏輯」，
# 差別只在於用 checkK 動態判斷每一組的邊界，而不是用固定的 left/right。
# 這印證了 Reorder List、Reverse Linked List II 反覆用到的工程手法：把看起來複雜
# 的題目拆解成「定位、斷開、處理、重新連接」的固定步驟，這題再加上一層「重複執行
# 這個固定步驟直到某個條件不成立」的外層迴圈。
# 攤銷分析：雖然 checkK 每組都要多走一次，但每個節點只會被檢查一次，整體仍是
# O(n)，不是 O(n*k) 這種重複計算。

# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prevNode = dummy  # 目前這一組前面那個節點

        def checkK(node, k):
            # 檢查從 node 開始是否存在 k 個節點
            for i in range(k):
                if node == None:
                    return False
                node = node.next
            return True

        while True:
            if checkK(prevNode.next, k):
                tmp = prevNode.next  # 這一組的起點
                prevNode.next = None
                end = tmp
                for i in range(k - 1):
                    end = end.next    # end 走到這一組的最後一個節點
                tmp2 = end.next        # 先存下後段起點，斷開後才找得到
                end.next = None         # 斷開後面，這一組變成獨立小串列

                # 標準三指標反轉
                cur = tmp
                prev = None
                while cur:
                    saveNext = cur.next
                    cur.next = prev
                    prev = cur
                    cur = saveNext

                prevNode.next = prev  # 接到反轉後的新起點
                tmp.next = tmp2         # 反轉後的新尾巴接到後段
                prevNode = tmp           # 移動到下一組的「前面那個節點」
            else:
                break  # 剩餘節點不足 k 個，保持原樣，結束

        return dummy.next