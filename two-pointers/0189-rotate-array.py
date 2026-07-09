# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
# 難度：Medium
# 類型：Two Pointers

# 思路：
# 把陣列往右旋轉 k 步，用「三次反轉法」in-place 完成。
# 因為 k 可能大於陣列長度（旋轉一整圈等於沒轉），先用 k % len(nums) 算出實際要旋轉幾步。
# 直覺理解：
# 1. 先把整個陣列反轉一次，這樣「原本在陣列尾端的 k 個元素」會被移到陣列最前面，
#    「原本在前面的元素」會被擠到後面——大方向的位置對了，但兩個區塊內部的相對順序都反了。
# 2. 再把前 k 個位置（索引 0 到 n-1）反轉一次，修正前段區塊內部的順序。
# 3. 最後把剩下的部分（索引 n 到最後）反轉一次，修正後段區塊內部的順序。
# 三次反轉都是用 Reverse String 學過的左右指標對撞技巧，只是每次呼叫的範圍不同。

# Pattern 筆記：
# 這題的 pattern 是「三次反轉法（reverse-reverse-reverse）」，
# 下次看到「陣列/字串需要 in-place 旋轉或平移」的特徵，
# 可以考慮先整體反轉再分段反轉，用反轉的組合達成平移的效果。

# Time: O(n)，三次反轉各自處理陣列的一部分，加起來仍是線性
# Space: O(1)，in-place 修改，沒有額外資料結構

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = k % len(nums)

        # 第一次反轉：整個陣列
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # 第二次反轉：前 n 個位置，修正前段順序
        left, right = 0, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # 第三次反轉：剩下的部分，修正後段順序
        left, right = n, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1