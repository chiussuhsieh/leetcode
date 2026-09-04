# 0141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# 難度：Easy
# 類型：Linked List

# 思路：
# Brute force 解法：用一個 set 記錄走過的「節點」（不是 node.val，因為不同節點可能有相同的值，
# 只有節點本身的記憶體位置能唯一代表「有沒有走過」），每走一步就檢查目前節點是否已在 set 裡，
# 有的話代表繞回去了，就是 cycle。這個方法時間 O(n)、空間 O(n)。
#
# 更省空間的解法：Floyd's Cycle Detection（龜兔賽跑），用 fast、slow 兩個指標，
# slow 每次走 1 步、fast 每次走 2 步，兩者都從 head 出發。
# 如果 linked list 有 cycle，fast 會在圈內從後面追上 slow，兩者終將相遇（slow == fast）；
# 如果沒有 cycle，fast 會先走到底（fast 或 fast.next 變成 None），迴圈結束回傳 False。
#
# 迴圈條件要同時檢查 fast 和 fast.next 都不是 None，
# 因為 fast 每次要走兩步（fast = fast.next.next），如果只檢查 fast 不是 None，
# 但 fast.next 剛好是 None，對 None 呼叫 .next 會直接噴 AttributeError。

# Pattern 筆記：
# 這是「快慢指標（Floyd's Tortoise and Hare）」的基本 pattern，核心概念是：
# 如果結構中存在「循環」，用不同速度的兩個指標繞圈，快的終究會追上慢的。
# 之後遇到 Find The Duplicate Number（把陣列當成隱含的 linked list 來看，值當作下一個
# index），以及需要「找中點」的題目（Reorder List 等，slow 走一步、fast 走兩步，
# fast 走到底時 slow 剛好在中點），都是這個 pattern 的變形應用。
# 相遇不代表迴圈就此結束——如果題目要進一步問「cycle 從哪個節點開始」（Linked List Cycle II），
# 還需要在相遇後，讓其中一個指標回到 head、兩者改成一次各走一步，第二次相遇處就是 cycle 起點，
# 這是這個 pattern 的延伸考法，先記著。

# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head  # 快指標，每次走 2 步
        slow = head  # 慢指標，每次走 1 步
        while fast and fast.next:  # fast.next 也要檢查，避免對 None 呼叫 .next
            fast = fast.next.next  # fast 走兩步
            slow = slow.next       # slow 走一步
            if slow == fast:       # 兩指標相遇，代表有 cycle
                return True
        return False  # fast 先走到底，代表沒有 cycle