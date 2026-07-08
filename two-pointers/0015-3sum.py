# 15. 3Sum
# https://leetcode.com/problems/3sum/
# 難度：Medium
# 類型：Two Pointers

# 思路：
# 先把陣列排序，這樣就能延用 Two Sum II 的雙指標邏輯，同時方便處理去重。
# 用 for 迴圈固定第一個數字 arr[i]，把問題轉化成「在 i 右邊的區間找兩數之和等於 -arr[i]」。
# 內層用 left（從 i+1 開始）、right（陣列尾端）雙指標收斂：
#   總和太大就 right -= 1，太小就 left += 1，剛好等於就記錄答案。
# 去重分兩層：
#   1. 外層 i：如果 arr[i] 跟前一個 arr[i-1] 相同，代表這個固定值已經處理過，直接 continue 跳過。
#   2. 內層 left/right：找到一組答案後，持續跳過跟剛剛用過的值相同的新值，
#      避免同樣的數值組合被重複記錄，同時用 left < right 確保不會超出合法搜尋範圍。

# Pattern 筆記：
# 這題的 pattern 是「固定一個數字 + 排序後雙指標收斂（fix one + two pointers on sorted array）」，
# 下次看到「找 k 個數字加總等於特定值」且「結果不能重複」的特徵，
# 可以考慮排序後固定外層一個數字，把問題降階成雙指標的子問題，並在固定值跟指標移動時都加上去重邏輯。

# Time: O(n^2)，排序 O(n log n) + 外層 for O(n) * 內層雙指標 O(n)，取較大者
# Space: O(n)，sorted() 產生新陣列，不計入輸出結果 res 本身

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        arr = sorted(nums)
        res = []
        for i in range(len(arr)):
            # 跳過重複的固定值，避免重複組合
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            left = i + 1
            right = len(arr) - 1
            while left < right:
                if arr[left] + arr[right] == -arr[i]:
                    res.append([arr[i], arr[left], arr[right]])
                    left += 1
                    # 跳過跟剛剛用過的 left 值相同的新值
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    right -= 1
                    # 跳過跟剛剛用過的 right 值相同的新值
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1
                elif arr[left] + arr[right] > -arr[i]:
                    right -= 1
                else:
                    left += 1
        return res