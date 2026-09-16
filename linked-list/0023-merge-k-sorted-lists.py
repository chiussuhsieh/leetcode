# 0023. Merge K Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/
# 難度：Hard
# 類型：Linked List

# 思路：
# 最直覺的解法是「循序合併」：重複呼叫 mergeTwoLists，把 k 個串列一個一個
# 併進同一個累積結果裡。但這樣做，累積結果會越來越長，第 i 次合併要處理
# O(i*n) 個節點，總花費是等差數列 2n+3n+...+kn，數量級是 O(k²n)，效率不佳。
#
# 更優的解法是「分治合併」（兩兩配對）：把 k 個串列切成左右兩半，分別遞迴
# 合併成一個串列，再用 mergeTwoLists 把兩個結果合併起來。
# 這樣整個遞迴呼叫形成一棵切割樹，每一層串列數量減半，總共只有 O(log k) 層；
# 而不管怎麼切，每一層加總起來都要走訪過全部 k*n 個節點恰好一次，
# 所以整體時間複雜度是 O(kn log k)，比循序合併的 O(k²n) 快得多
# （這跟用迭代方式「兩兩合併」的推導是同一件事，只是這裡用遞迴實作）。
#
# Base case：lists 是空的回傳 None；只剩一個串列，本身就是答案，直接回傳。
# 遞迴切點用 mid = len(lists) // 2，left = lists[:mid]、
# right = lists[mid:]，分別遞迴呼叫 mergeKLists 合併成單一串列，
# 最後用標準的 mergeTwoLists（dummy node 技巧，源自這一章第 4 題）
# 合併兩個已排序的結果。

# Pattern 筆記：
# 這是這一章的壓軸整合題，把 Merge Two Sorted Lists 的合併邏輯，套用
# 「分治法（Divide and Conquer）」的框架重複使用。核心洞察是：與其讓單一
# 個累積結果不斷變長（循序合併，O(k²n)），不如讓合併的規模保持平衡
# （兩兩配對合併），把「串列數量減半」的過程換算成 O(log k) 層，這跟
# binary search 每次排除一半範圍是同樣的數學結構。
# 遞迴版本的空間複雜度來自 call stack 深度（O(log k)），這跟 Reverse
# Linked List 提過的「iterative O(1) vs recursive O(n)」是同一種分析
# 方式，只是這裡的深度是 log k 而不是 n，因為每層都讓問題規模減半而非
# 減一。這個「切分問題規模、遞迴解決子問題、合併結果」的框架，
# 之後遇到任何「多個已排序資料源要合併」的題目都可以優先考慮。

# Time complexity: O(kn log k)，k 為串列數量，n 為每個串列的平均長度
# Space complexity: O(log k)，遞迴 call stack 深度（不計輸出結果）

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])   # 遞迴合併前半
        right = self.mergeKLists(lists[mid:])  # 遞迴合併後半
        return self.merge2Lists(left, right)   # 合併兩個已排序結果

    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1  # 剩餘的部分本身已排序好，直接整段接上
        if l2:
            cur.next = l2
        return dummy.next