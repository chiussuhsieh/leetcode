# 0410. Split Array Largest Sum
# https://leetcode.com/problems/split-array-largest-sum/
# 難度：Hard
# 類型：Binary Search

# 思路：
# 這題要找的答案是「k 份分割裡最大子陣列和的最小可能值」，在答案空間上做 binary search。
# 下界是 max(nums)：因為最大的單一元素無論怎麼分割，都會落在某一組裡，那一組的和至少是這個元素本身，
# 所以答案不可能小於 max(nums)。
# 上界是 sum(nums)：對應 k = 1 的情況，全部數字都在同一組。
# left 設 max(nums)，right 設 sum(nums)，用 while left < right 持續搜尋
# （因為合格時要保留 middle，middle 本身可能就是最小可行值，不能排除）。
# 每一輪先把 subNeeded 歸零成 1（第一組本來就要算進去）、curArrSum 歸零成 0，
# middle 取中間值當作這一輪猜測的「每組和上限」。
# 用內層 for 迴圈模擬：依序把每個數字加進目前這一組的和 curArrSum，
# 如果加上這個數字會超過 middle（這組裝不下了），就開新的一組（subNeeded += 1），
# 並讓這個數字成為新一組的第一個元素（curArrSum = num）；否則繼續累加進目前這組。
# 如果 subNeeded > k，代表這個 middle 上限太小，需要分的組數超過 k，不可行，
# 要往更大的上限找，left 移到 middle + 1。
# 否則代表這個 middle 是可行候選（能用 k 份或更少分完），但可能還有更小的可行值，
# right 移到 middle（不 -1，因為 middle 本身可能就是最小可行值，不能排除）。
# 迴圈結束時 left == right，就是最小的最大子陣列和。
# 這個結果之所以保證正確，是因為只要 middle 比真正答案小，內層函式一定會誠實地回報「不可行」
# （subNeeded > k），binary search 就會往更大的方向排除它；只有在真正的最小可行值，內層函式
# 才會回報「可行」，且它是所有可行值裡最小的那個。

# Pattern 筆記：
# 這題的 pattern 是 binary search on answer space，結構跟 0875 Koko Eating Bananas、
# 1011 Ship Within D Days 完全平行：下次看到「要找滿足條件的最小數值上限、且該數值具有單調性
# （上限越大所需的分組/天數越少）」的特徵就用這個方法。內層計算邏輯是依序累加、超過上限就開新一組，
# 外層骨架一致：可行時 right = middle（保留候選），不可行時 left = middle + 1，搭配 while left < right。

# Time complexity: O(n log(sum(nums) - max(nums)))，n 為 nums 長度
# Space complexity: O(1)

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)  # 最大子陣列和的最小可能值
        right = sum(nums)  # 最大子陣列和的最大可能值（k = 1 的情況）
        while left < right:  # 左右邊界還沒相遇就繼續找
            subNeeded = 1  # 每一輪重新計算，第一組本來就要算進去
            curArrSum = 0  # 每一輪重新計算目前這組的和
            middle = (left + right) // 2  # 這一輪猜測的每組和上限
            for num in nums:  # 依序模擬分組過程
                if curArrSum + num > middle:  # 這組裝不下了，開新的一組
                    subNeeded += 1
                    curArrSum = num
                else:  # 這組還裝得下，繼續累加
                    curArrSum += num
            if subNeeded > k:  # 上限太小，需要的組數超過 k，不可行
                left = middle + 1
            else:  # 上限夠大，是可行候選（保留 middle）
                right = middle
        return left  # left 和 right 相遇的位置就是最小的最大子陣列和