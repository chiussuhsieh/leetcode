# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
# 難度：Easy
# 類型：Two Pointers

# 思路：
# nums1 前 m 個是有效資料，後面是空位；nums2 長度 n，兩個都已排序好。
# 因為要 in-place 修改，如果從前面開始比較填入，會覆蓋掉 nums1 還沒比較過的資料。
# 所以改成從「後面」往前填：
# p1 指向 nums1 有效資料的尾端（m-1），p2 指向 nums2 的尾端（n-1），
# write 指向 nums1 整個陣列的最後一格（m+n-1），也就是目前要寫入的位置。
# 每輪比較 nums1[p1] 和 nums2[p2]，把較大的放到 write 位置，對應的指標往前移一格，write 也往前移一格。
# 三種情況：
# 1. p1、p2 都還沒放完：正常比大小，放較大的
# 2. p2 已經放完（p2 < 0），p1 還有剩：代表 nums1 剩下的元素本來就比已經放進去的數字小，
#    位置已經是對的，不需要再搬動，直接 break 結束迴圈
# 3. p1 已經放完（p1 < 0），p2 還有剩：nums2 剩下的元素還留在 nums2 陣列裡，
#    必須手動搬到 nums1 對應位置，不然 nums1 前面會維持原本填充的 0

# Pattern 筆記：
# 這題的 pattern 是「從後往前的雙指標合併（reverse merge two pointers）」，
# 下次看到「in-place 合併兩個排序陣列」且「其中一個陣列尾端有多餘空間可利用」的特徵就用這個方法。

# Time: O(m + n)
# Space: O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        write = m + n - 1

        while p1 >= 0 or p2 >= 0:
            if p1 >= 0 and p2 >= 0:
                # 兩邊都還有資料，比大小，放較大的到 write 位置
                if nums1[p1] > nums2[p2]:
                    nums1[write] = nums1[p1]
                    write -= 1
                    p1 -= 1
                else:
                    nums1[write] = nums2[p2]
                    write -= 1
                    p2 -= 1
            elif p1 >= 0 and p2 < 0:
                # nums2 已經放完，nums1 剩下的資料位置本來就是對的，不用搬動
                break
            else:
                # nums1 原始資料已經放完，把 nums2 剩下的元素搬過去
                nums1[write] = nums2[p2]
                write -= 1
                p2 -= 1