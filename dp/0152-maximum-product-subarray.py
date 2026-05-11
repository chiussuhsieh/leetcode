# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
# 難度：Medium
# 類型：DP

# 思路：
# 每個位置同時追蹤最大值和最小值
# 因為負數 * 負數 = 正數，最小值可能在下一步變成最大值
# 每次更新都要考慮三種情況：
# 1. 從這裡重新開始（nums[i]）
# 2. 最大值 * nums[i]
# 3. 最小值 * nums[i]

# Time: O(n)
# Space: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]   # 到目前為止的最大乘積
        min_prod = nums[0]   # 到目前為止的最小乘積（負數 * 負數 可能變最大）
        result = nums[0]     # 全局最大乘積

        for i in range(1, len(nums)):
            # 先把三種情況都算出來
            candidates = (nums[i], max_prod * nums[i], min_prod * nums[i])
            # nums[i]：從這裡重新開始（前面的乘積不如不要）
            # max_prod * nums[i]：延續最大乘積
            # min_prod * nums[i]：最小乘積 * 負數 = 可能變最大

            max_prod = max(candidates)   # 更新最大乘積
            min_prod = min(candidates)   # 更新最小乘積

            result = max(result, max_prod)   # 更新全局最大乘積

        return result