# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# 難度：Easy
# 類型：Two Pointers

# 思路：
# 先把字串轉小寫，再過濾掉所有非英文字母、非數字的字元，組成一個新字串 newS。
# 用左右指標從 newS 的頭尾開始往中間比較，只要有一對字元不相等就回傳 False。
# 如果字串長度是奇數，中間那個字元因為前後對稱，left == right 時迴圈自然停止，
# 不需要額外處理（跟 Reverse String 的觀察一樣）。
# 空字串（過濾完全部字元都不是英數字元）視為合法迴文，直接回傳 True。

# Pattern 筆記：
# 這題的 pattern 是「前處理 + 左右指標對撞（preprocess then opposite direction two pointers）」，
# 下次看到「需要忽略特定字元或大小寫再判斷迴文/對稱性」的特徵，
# 可以先做一次前處理（過濾、轉換大小寫），把問題簡化成單純的左右指標比較。

# Time: O(n)，過濾字元 O(n) + 雙指標比較 O(n)
# Space: O(n)，newS 是額外建立的新字串

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS = s.lower()
        newS = ""
        for i in range(len(lowerS)):
            # 只保留英文字母和數字
            if lowerS[i].isalnum():
                newS += lowerS[i]

        left, right = 0, len(newS) - 1
        if newS == "":
            return True

        while left < right:
            if newS[left] != newS[right]:
                return False
            left += 1
            right -= 1

        return True