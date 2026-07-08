# 18. 4Sum
# https://leetcode.com/problems/4sum/
# 難度：Medium
# 類型：Two Pointers

# 思路：
# 延伸 3Sum 的做法，多包一層迴圈。先排序陣列，
# 用兩層 for 迴圈固定 i、j 兩個數字（j 從 i+1 開始），
# 把問題轉化成「在 j 右邊的區間找兩數之和，讓四數總和等於 target」。
# 內層用 left（從 j+1 開始）、right（陣列尾端）雙指標收斂：
#   四數總和太大就 right -= 1，太小就 left += 1，剛好等於就記錄答案。
# 去重分三層：
#   1. i：如果 arr[i] 跟前一個 arr[i-1] 相同（且 i > 0），代表這個固定值處理過，跳過。
#   2. j：如果 arr[j] 跟前一個 arr[j-1] 相同（且 j > i+1，確保不是跟 i 搞混的第一輪），跳過。
#   3. left/right：找到答案後，持續跳過跟剛剛用過的值相同的新值，
#      並用 left < right 確保不超出合法搜尋範圍。

# Pattern 筆記：
# 這題的 pattern 是「固定兩個數字 + 排序後雙指標收斂（fix two + two pointers on sorted array）」，
# 是 3Sum 的直接延伸：k-sum 問題可以透過「固定 k-2 個數字，把問題降階成雙指標找剩下兩個數字」
# 這個模式來解決，每多固定一個數字就多包一層迴圈，並各自加上對應的去重邏輯。

# Time: O(n^3)，排序 O(n log n) + 兩層 for O(n^2) * 內層雙指標 O(n)，取較大者
# Space: O(n)，sorted() 產生新陣列，不計入輸出結果 res 本身

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr = sorted(nums)
        res = []
        for i in range(len(arr)):
            # 跳過重複的 i，避免重複組合
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            for j in range(i + 1, len(arr)):
                # 跳過重複的 j（確保是同一個 i 底下的第二輪以後才比較）
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                left = j + 1
                right = len(arr) - 1
                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]
                    if total == target:
                        res.append([arr[i], arr[j], arr[left], arr[right]])
                        left += 1
                        # 跳過跟剛剛用過的 left 值相同的新值
                        while left < right and arr[left] == arr[left - 1]:
                            left += 1
                        right -= 1
                        # 跳過跟剛剛用過的 right 值相同的新值
                        while left < right and arr[right] == arr[right + 1]:
                            right -= 1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1
        return res