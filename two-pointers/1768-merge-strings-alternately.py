# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/
# 難度：Easy
# 類型：Two Pointers

# 思路：
# 用兩個指標 left、right 分別追蹤目前讀到 word1、word2 的第幾個字元。
# 用一個 while 迴圈，只要 left 或 right 其中一個還沒超出各自字串的長度就繼續跑。
# 迴圈內先檢查 left 有沒有超出 word1 範圍，沒有的話就把該字元加進結果字串、left 前進一格；
# 再用同樣邏輯檢查 right 跟 word2。
# 因為用的是 if 而不是 elif，所以哪一邊還沒跑完就會自動繼續加，
# 跑完的那一邊 if 判斷會直接跳過，不需要額外處理「補上剩餘字串」的邏輯。

# Pattern 筆記：
# 這題的 pattern 是「雙指標平行前進（parallel two pointers）」，
# 兩個指標分別獨立追蹤兩個不同來源的進度，不是頭尾對撞。
# 下次看到「交替合併兩個序列」或「兩個獨立長度不同的輸入需要同步處理」的特徵就用這個方法。

# Time: O(m + n)，m、n 分別是 word1、word2 的長度
# Space: O(m + n)，字串是 immutable，每次 += 都會產生新字串，最終結果字串本身也佔空間

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        newWord = ""
        while left < len(word1) or right < len(word2):
            # 如果 word1 還沒讀完，加入目前 left 指向的字元
            if left < len(word1):
                newWord += word1[left]
                left += 1
            # 如果 word2 還沒讀完，加入目前 right 指向的字元
            if right < len(word2):
                newWord += word2[right]
                right += 1
        return newWord