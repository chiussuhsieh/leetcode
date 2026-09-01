# 0004. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# 難度：Hard
# 類型：Binary Search

# 思路：
# 這題要求時間複雜度 O(log(m+n))，代表不能真的合併兩個陣列（那至少要 O(m+n)），
# 必須用 binary search 直接定位 median，不實際合併。
#
# 核心概念是「partition（切割）」：把 nums1 切成左右兩半，nums2 也切成左右兩半，
# 使得兩邊「左半」的元素個數加起來，剛好等於 median 前面應該有的數字個數
# （half = (m+n+1)//2，這個 +1 讓奇偶都能用同一套公式：奇數時左半比右半多一個，
# median 就是左半最大值；偶數時左右對半分，median 是左半最大值和右半最小值的平均）。
#
# 先確保 nums1 是較短的陣列（交換），binary search 只對 nums1 的切點數量做，
# nums2 的切點數量可以直接用 half - middleA 算出來，不需要對兩個陣列都搜尋，
# 這樣複雜度是 O(log(min(m,n)))。
# left 設 0，right 設 len(nums1)，代表 nums1 左半元素個數的可能範圍
# （0 代表左半全空，len(nums1) 代表全部都在左半）。
#
# 每一輪算出 middleA（nums1 左半個數）、middleB = half - middleA（nums2 左半個數），
# 取出四個關鍵值：nums1 左半最後一個（nums1LeftMax）、nums1 右半第一個（nums1RightMin）、
# nums2 左半最後一個（nums2LeftMax）、nums2 右半第一個（nums2RightMin）。
# 如果某一半是空的（middleA/middleB 為 0 或等於陣列長度），用 -inf 代表不存在的左半最大值、
# 用 inf 代表不存在的右半最小值，這樣不會影響後續的大小比較。
#
# 合法性判斷：nums1LeftMax <= nums2RightMin 且 nums2LeftMax <= nums1RightMin。
# 如果合法，代表找到正確的切點，依照 (m+n) 奇偶回傳對應的 median。
# 如果不合法，且 nums1LeftMax > nums2RightMin，代表 nums1 切太多了（左半的東西太大），
# 要往左調整，right = middleA - 1；否則代表 nums1 切太少了，left = middleA + 1。

# Pattern 筆記：
# 這題的 pattern 是「用 binary search 找一個 partition（切點），使得兩個已排序陣列
# 切出來的左右兩半滿足大小關係」，下次看到「兩個已排序陣列 + 要求 O(log(m+n)) 複雜度」
# 的特徵就用這個方法。關鍵是只需要對較短的陣列做 binary search，另一邊的切點用總數反推。

# Time complexity: O(log(min(m, n)))
# Space complexity: O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):  # 確保 nums1 是較短的陣列
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        half = (m + n + 1) // 2  # 左半總共應該要有幾個元素（同時處理奇偶）
        left = 0  # nums1 切點數量的搜尋範圍下界
        right = m  # nums1 切點數量的搜尋範圍上界
        while left <= right:
            middleA = (left + right) // 2  # nums1 左半的元素個數
            middleB = half - middleA  # nums2 左半的元素個數（由總數反推）

            # 取出四個關鍵值，空的那一半用 inf / -inf 代表
            nums1LeftMax = -float("inf") if not middleA else nums1[middleA - 1]
            nums1RightMin = float("inf") if middleA == m else nums1[middleA]
            nums2LeftMax = -float("inf") if not middleB else nums2[middleB - 1]
            nums2RightMin = float("inf") if middleB == n else nums2[middleB]

            if nums1LeftMax <= nums2RightMin and nums2LeftMax <= nums1RightMin:  # 切法合法
                if (m + n) % 2:  # 總長度是奇數，median 是左半最大值
                    return max(nums1LeftMax, nums2LeftMax)
                else:  # 總長度是偶數，median 是左半最大值和右半最小值的平均
                    return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2
            else:
                if nums1LeftMax > nums2RightMin:  # nums1 切太多了，往左調整
                    right = middleA - 1
                else:  # nums1 切太少了，往右調整
                    left = middleA + 1