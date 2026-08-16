# 1011. Capacity to Ship Packages Within D Days
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# 難度：Medium
# 類型：Binary Search

# 思路：
# 這題要找的答案是船的最小載重容量 capacity，在「答案空間」上做 binary search。
# capacity 的可能範圍：最小不能小於單一包裹裡最重的那個（不然那包永遠裝不上船），
# 所以 left 設 max(weights)；最大則是一天把所有包裹一次裝完，所以 right 設 sum(weights)。
# 用 while left < right 持續搜尋（因為合格時要保留 middle，不能排除，見下方說明）。
# 每一輪先把 daysNeeded 歸零成 1（第一天本來就要算進去）、dayWeights 歸零成 0。
# 用內層 for 迴圈模擬：依序把每個包裹的重量加進今天的 dayWeights，
# 如果加上這個包裹會超過 middle（今天裝不下了），就換到新的一天（daysNeeded += 1），
# 並讓這個包裹成為新一天的第一個重量（dayWeights = w）；否則就繼續裝進今天（dayWeights += w）。
# 如果算出來的 daysNeeded > days，代表這個 middle 容量太小，天數超過限制，不合格，
# 要往更大的容量找，left 移到 middle + 1。
# 否則代表這個 middle 是合格候選（天數在限制內），但可能還有更小的合格值，
# right 移到 middle（不 -1，因為 middle 本身可能就是最小合格容量，不能排除）。
# 迴圈結束時 left == right，就是最小合格容量。

# Pattern 筆記：
# 這題的 pattern 是 binary search on answer space，結構跟 0875 Koko Eating Bananas 完全平行：
# 下次看到「要找滿足條件的最小數值、且該數值具有單調性（容量越大天數越少）」的特徵就用這個方法。
# 內層計算邏輯不同（這題是依序累加、超過就換一天，不是用除法），但外層 binary search 骨架一致：
# 合格時 right = middle（保留候選），不合格時 left = middle + 1，搭配 while left < right。

# Time complexity: O(n log(sum(weights) - max(weights)))，n 為 weights 長度
# Space complexity: O(1)

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)  # capacity 最小可能值
        right = sum(weights)  # capacity 最大可能值
        while left < right:  # 左右邊界還沒相遇就繼續找
            daysNeeded = 1  # 每一輪重新計算，第一天本來就要算進去
            dayWeights = 0  # 每一輪重新計算今天已裝的重量
            middle = (left + right) // 2  # 這一輪猜測的容量
            for w in weights:  # 依序模擬裝船過程
                if dayWeights + w > middle:  # 今天裝不下了，換新的一天
                    daysNeeded += 1
                    dayWeights = w
                else:  # 今天還裝得下，繼續裝
                    dayWeights += w
            if daysNeeded > days:  # 容量太小，天數超過限制，不合格
                left = middle + 1
            else:  # 容量夠大，是合格候選（保留 middle）
                right = middle
        return left  # left 和 right 相遇的位置就是最小合格容量