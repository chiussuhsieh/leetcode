# 312. Burst Balloons
# https://leetcode.com/problems/burst-balloons/
# 難度：Hard
# 類型：2D DP (區間 DP)

# 思路：
# 正向思考「先戳哪個」很難，因為戳破之後左右會變成相鄰，互相影響
# 反過來想：對於區間 (left, right)，思考「最後一個戳破的氣球是誰」
# 因為最後戳破時，這個氣球的左右邊界就是 nums[left] 和 nums[right]（不會再變了）
# dp[left][right] = 戳破 (left, right) 之間所有氣球的最大分數（不包含 left, right 本身）
# 對每個可能的 "最後戳破的氣球" i，分數 = 左邊全部戳完的分數 + 右邊全部戳完的分數
#                                    + nums[left] * nums[i] * nums[right]
# 在頭尾各加一個虛擬氣球 1，方便處理邊界

# Time: O(n^3)
# Space: O(n^2)

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]   # 頭尾加上虛擬氣球，方便處理邊界
        n = len(nums)

        dp = {}   # key=(left, right)，value=戳破這個區間的最大分數

        def solve(left, right):
            if left + 1 == right:
                return 0   # 中間沒有氣球可以戳了

            if (left, right) in dp:
                return dp[(left, right)]

            best = 0
            for i in range(left + 1, right):
                # 假設 i 是這個區間「最後一個」被戳破的氣球
                coins = nums[left] * nums[i] * nums[right]
                coins += solve(left, i) + solve(i, right)
                # 左半邊和右半邊各自先戳完，因為 i 最後戳，左右邊界不會被影響
                best = max(best, coins)

            dp[(left, right)] = best
            return best

        return solve(0, n - 1)