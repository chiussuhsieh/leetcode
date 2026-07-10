# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/
# 難度：Easy
# 類型：Two Pointers

# 思路：
# 用左右指標從頭尾開始往中間比較，跟 Valid Palindrome 一樣。
# 如果 s[left] == s[right]，正常移動指標繼續比較。
# 如果 s[left] != s[right]，代表這裡卡住了，最多只能刪一個字元，
# 所以嘗試兩種可能：
#   1. 刪掉 s[left]：檢查 s[left+1:right+1] 這段是否為迴文
#   2. 刪掉 s[right]：檢查 s[left:right] 這段是否為迴文
# 分別用兩組獨立的指標（l1/r1、l2/r2）和布林旗標（is_valid_1、is_valid_2）檢查，
# 遇到不匹配就把對應旗標設成 False 並 break（不用 return，避免影響另一組檢查）。
# 只要其中一種可能是迴文，整體就回傳 True；兩種都不是才回傳 False。
# 這裡在確定不匹配、算完兩種可能後直接 return，避免外層迴圈繼續跑、覆蓋掉這兩個變數。
# 如果整個字串從頭到尾都沒有遇到不匹配，代表原本就是迴文，回傳 True。

# Pattern 筆記：
# 這題的 pattern 是「雙指標對撞 + 一次容錯分支嘗試（two pointers with one-time branching）」，
# 下次看到「允許刪除/修改最多一個元素，判斷是否滿足某個對稱或排序性質」的特徵，
# 可以在雙指標比對失敗的當下，分別嘗試「跳過左邊」或「跳過右邊」兩種可能，
# 並用獨立的旗標記錄結果，只要有一種可行就成立。

# Time: O(n)，外層迴圈跟兩個內層迴圈是「二選一」關係，不是巢狀相乘，加總仍是線性
# Space: O(1)，只用了幾個指標和布林變數，沒有額外資料結構

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # 嘗試 1：刪掉 s[left]
                l1, r1 = left + 1, right
                is_valid_1 = True
                while l1 < r1:
                    if s[l1] != s[r1]:
                        is_valid_1 = False
                        break
                    l1 += 1
                    r1 -= 1

                # 嘗試 2：刪掉 s[right]
                l2, r2 = left, right - 1
                is_valid_2 = True
                while l2 < r2:
                    if s[l2] != s[r2]:
                        is_valid_2 = False
                        break
                    l2 += 1
                    r2 -= 1

                return is_valid_1 or is_valid_2

            left += 1
            right -= 1

        return True