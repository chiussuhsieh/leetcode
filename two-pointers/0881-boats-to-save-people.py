# 881. Boats to Save People
# https://leetcode.com/problems/boats-to-save-people/
# 難度：Medium
# 類型：Two Pointers

# 思路：
# 先排序，讓 left 指向最輕的人、right 指向最重的人。
# 貪心策略：優先嘗試讓最重的人跟最輕的人配對，因為如果連最輕的人都無法跟最重的人配對，
# 最重的人就沒有機會跟任何其他人（更重的人）配對了，只能自己一艘船。
# 兩種情況：
# 1. nums[left] + nums[right] > limit（超重）：最重的人（right）只能自己坐一艘船，
#    right -= 1（處理完這個人），left 不動（他還有機會跟下一個次重的人配對），boats += 1。
# 2. nums[left] + nums[right] <= limit（沒超重）：兩人可以共乘一艘船，
#    left += 1 和 right -= 1 都要移動（兩人都被安排了），boats += 1。
# 迴圈用 left <= right（不是 left < right），因為當只剩最後一人時，
# 這個人自己也還需要一艘船，要被計算進去。

# Pattern 筆記：
# 這題的 pattern 是「排序後貪心雙指標配對（greedy pairing with two pointers）」，
# 跟 Container With Most Water 很像，都是排序或收斂後從兩端逼近，
# 下次看到「配對問題」且「其中一方越極端（越重/越大）越難搭配、要優先驗證能否配對」的特徵就用這個方法。

# Time: O(n log n)，排序主導整體複雜度
# Space: O(n)，sorted() 產生新陣列

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        nums = sorted(people)
        left, right = 0, len(nums) - 1
        boat = 0

        while left <= right:
            if nums[left] + nums[right] > limit:
                # 最重的人超重無法配對，自己一艘船
                boat += 1
                right -= 1
            else:
                # 兩人可以共乘一艘船
                boat += 1
                left += 1
                right -= 1

        return boat