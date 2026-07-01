# 912. Sort an Array
# https://leetcode.com/problems/sort-an-array/
# 難度：Medium
# 類型：Array, Sorting, Divide and Conquer
# 思路：
# 用 Merge Sort 分治法
# mergeSort 負責遞迴切割 array 到只剩一個元素（base case）
# merge 負責合併兩個已排好序的 array，用兩個指針比大小依序放進 result
# 剩下的元素可以直接 append，因為兩邊都已排好序
# Pattern 筆記：
# 這題的 pattern 是「Merge Sort 分治法」
# mergeSort → 負責遞迴切割到 base case
# merge → 負責合併兩個已排序的 array，剩下的直接 append
# 下次看到「需要 O(n log n) 排序且不能用內建 sort」就用這個方法
# Time: O(n log n)
# Space: O(n)

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left, right):
            result = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])  # 左邊比較小，放左邊
                    i += 1
                else:
                    result.append(right[j]) # 右邊比較小，放右邊
                    j += 1
            while i < len(left):
                result.append(left[i])      # 左邊還有剩，直接全部加進去
                i += 1
            while j < len(right):
                result.append(right[j])     # 右邊還有剩，直接全部加進去
                j += 1
            return result

        def mergeSort(array):
            if len(array) <= 1:             # base case：只有一個元素，直接回傳
                return array
            mid = len(array) // 2
            left = mergeSort(array[:mid])   # 遞迴排序左半
            right = mergeSort(array[mid:])  # 遞迴排序右半
            return merge(left, right)       # 合併兩個排好的 array

        return mergeSort(nums)