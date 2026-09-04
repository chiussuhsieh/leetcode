# 0021. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# 難度：Easy
# 類型：Linked List

# 思路：
# 用兩個指標分別走訪 list1、list2，每次比較兩者目前節點的值，較小的接到結果串列，
# 該串列的指標往前走一步。
#
# 因為結果串列一開始是空的，head 到底是 list1 還是 list2 的第一個節點，要等比較過
# 才能確定，所以用 dummy node（哨兵節點）當起點，讓所有節點（包含第一個）都能用
# 同一套「cur.next = ...」邏輯處理，不需要額外判斷 head 特殊情況。
#
# 主迴圈跑到其中一個串列走完為止。走完後，剩下還沒走完的那個串列本身已經排序好，
# 不需要逐一比較接上去，直接一行 cur.next = list1 if list1 else list2 接上剩餘部分即可。
#
# 最後回傳 dummy.next（dummy 本身是假節點，真正的 head 是它的 next）。

# Pattern 筆記：
# 這是 dummy node 技巧的起手式：只要「結果串列的 head 不確定該是誰」，就可以用
# dummy + cur 兩個指標簡化「第一個節點特殊處理」的問題。
# 之後遇到 Remove Nth Node From End of List、Reorder List、Merge K Sorted Lists
# 都會延伸用到這個技巧，Merge K Sorted Lists 更是直接把這題的合併邏輯擴展到多個串列
# （搭配 heap 做 k 路合併）。

# Time complexity: O(m + n)，m、n 分別為 list1、list2 的長度
# Space complexity: O(1)，只重新接 next 指標，沒有建立新節點資料

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # 哨兵節點，本身不算數，方便處理 head 不確定的情況
        cur = dummy         # cur 指向結果串列目前的尾巴
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1   # 把較小的節點接到結果串列尾巴
                list1 = list1.next # list1 指標往前走一步
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next  # cur 也往前推進到剛接上去的節點
        # 其中一個串列已走完，剩下的另一個本身已排序好，直接整段接上去
        if list1 or list2:
            cur.next = list1 if list1 else list2
        return dummy.next  # dummy 是假節點，真正的 head 是它的 next