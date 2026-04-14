class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) # 房子總數
        dp = [0] * n # dp[i] = 搶到第 i 間時，能搶到的最大金額
        dp[0] = nums[0] # 只有一間房，直接搶
        dp[1] = nums[1] # 直接選第二間房搶
        if n <= 2:
            return max(dp[0], dp[1])  # 兩間以內，選金額較大的搶
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            # 兩個選擇取較大的：
            # 1. 搶第 i 間：nums[i] + dp[i-2]（上一間不能搶，跳到 i-2）
            # 2. 不搶第 i 間：dp[i-1]（維持上一間的最大金額）
        return dp[n - 1]
        # dp[n-1] 已經包含「搶或不搶最後一間」的最優解，直接回傳
    