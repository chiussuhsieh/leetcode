class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) # 樓梯總階數
        dp = [0] * n  # 建立 dp 陣列，dp[i] = 踩到第 i 階的最小花費
        dp[0] = cost[0] # 從第 0 階出發，花費就是 cost[0]
        dp[1] = cost[1] # 從第 1 階出發，花費就是 cost[1]
        if n <= 2:
            return min(dp[0], dp[1]) # 只有兩階的話，直接選花費較小的出發點
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
            # 到達第 i 階有兩種方式：
            # 從 i-1 跳一階上來，或從 i-2 跳兩階上來
            # 選花費較小的那條路，再加上踩這階的 cost[i]
        return min(dp[n - 1], dp[n - 2])
        # 終點是超過最後一階（不是最後一階本身）
        # 最後一步可以從 n-1 跳一階，或從 n-2 跳兩階
        # 選兩者中花費較小的