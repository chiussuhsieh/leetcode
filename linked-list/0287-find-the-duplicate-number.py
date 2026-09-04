# 0287. Find The Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/
# 難度：Medium
# 類型：Linked List（Floyd's Cycle Detection 應用於陣列）

# 思路：
# 陣列長度為 n+1，值域為 [1, n]，保證至少一個數字重複。
# 把「index i」看成一個節點，「nums[i]」當作「下一步要走到的 index」，
# 這樣陣列就變成一個 functional graph（每個節點恰有一條出邊），跟 linked list 的
# next 指標結構完全對應。
#
# 因為值域是 [1, n]（不含 0），index 0 不會被任何值指向，是安全的起點；
# 又因為有 n+1 個 index 但只有 n 種可能的值，根據鴿籠原理，一定有兩個不同 index
# 指向同一個下一步，路徑會在該處匯流，形成一個圈。而這個「重複的數字」正好就是
# 圈的入口（entry point），因為有兩條不同路徑走到它。這跟 Linked List Cycle II
# （找環的起點）是同一個問題。
#
# 解法分兩階段，都用 Floyd's Cycle Detection：
# 第一階段：slow 走 1 步（nums[slow]）、fast 走 2 步（nums[nums[fast]]），
# 兩者都從 index 0 出發，直到相遇（相遇點在圈內某處，不一定是入口）。
# 用 while True 搭配內部 break，避免「兩者一開始都是 0」導致迴圈條件誤判。
#
# 第二階段：設起點到入口距離為 a、入口到相遇點距離為 b、圈長為 c，
# 可推導出 a = c - b，因此讓一個指標從 index 0 出發、另一個留在第一階段的相遇點，
# 兩者都改成一次走 1 步，會同時抵達入口，那就是答案（重複的數字）。

# Pattern 筆記：
# 這題是 Linked List Cycle 的快慢指標 pattern 直接遷移到陣列上的應用，
# 核心轉換是把「index + nums[index]」重新詮釋成「節點 + next 指標」。
# 找圈的入口（而不只是判斷有沒有圈）的兩階段做法，跟 Linked List Cycle II
# 是同一套邏輯，之後遇到類似題目可以直接套用這個兩階段模板。

# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # 第一階段：快慢指標找相遇點（圈內某處，不一定是入口）
        while True:
            slow = nums[slow]        # 走一步
            fast = nums[nums[fast]]  # 走兩步
            if slow == fast:
                break

        # 第二階段：一個指標回到起點，另一個留在相遇點，兩者都走 1 步，直到相遇即為入口
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow