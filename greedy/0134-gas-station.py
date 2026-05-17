# 134. Gas Station
# https://leetcode.com/problems/gas-station/
# 難度：Medium
# 類型：Greedy

# 思路：
# 兩個關鍵觀察：
# 1. 如果 sum(gas) < sum(cost)，不管從哪裡出發都不可能完成，直接回傳 -1
# 2. 從左到右累積油量，如果 tank < 0，代表從之前的起點出發撐不到這裡
#    起點重設為 i+1，油箱歸零重新開始
# 題目保證答案唯一，所以最後的 start 就是答案

# Time: O(n)
# Space: O(1)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1          # 總油量不夠，不可能完成一圈

        tank = 0               # 目前油箱的油量
        start = 0              # 出發點

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            # 在第 i 站加油，然後扣掉到下一站的油耗
            # 累積油量，不重置，因為油箱是一直帶著走的

            if tank < 0:
                start = i + 1  # 從之前的起點出發撐不到這裡，起點重設為 i+1
                tank = 0       # 油箱歸零，從新起點重新開始

        return start           # 題目保證答案唯一，最後的 start 就是答案