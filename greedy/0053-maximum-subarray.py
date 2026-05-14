# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# 難度：Medium
# 類型：Greedy

# 思路：
# 從左到右掃，每個位置決定要繼續延伸還是重新開始
# 如果前面的總和是負數，帶著負數只會讓結果更小，不如從這裡重新開始
# 每次更新 maxSub，記錄目前找到的最大總和

# Time: O(n)
# Space: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]   # 記錄目前最大的 subarray 總和
                           # 初始化成 nums[0]，因為至少要包含一個元素

        curSum = 0         # 記錄目前 subarray 的總和

        for n in nums:     # 從左到右掃每個元素
            if curSum < 0:
                curSum = 0 # 前面總和是負數，帶著只會拖累結果
                           # 不如從這裡重新開始

            curSum += n            # 把當前元素加進來
            maxSub = max(maxSub, curSum)   # 更新最大總和

        return maxSub      # 回傳最大 subarray 總和