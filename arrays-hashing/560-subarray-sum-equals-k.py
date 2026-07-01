# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
# 難度：Medium
# 類型：Array, HashMap, Prefix Sum
# 思路：
# subarray 總和 = prefixSum[j] - prefixSum[i]
# iterate 每個位置，累加 currentSum
# 查 hashmap 有沒有出現過 currentSum - k
# 有的話代表找到合法 subarray，count += hashmap[currentSum - k]
# 再把 currentSum 存進 hashmap
# Pattern 筆記：
# 這題的 pattern 是「Prefix Sum + HashMap」
# subarray 總和 = prefixSum[j] - prefixSum[i]
# iterate 到每個位置，查 hashmap 有沒有出現過 currentSum - k
# 有的話代表找到合法 subarray，count += hashmap[currentSum - k]
# 初始化 hashmap = {0: 1} 處理從 index 0 開始的 subarray
# 下次看到「subarray 總和等於 k，array 有負數」就用這個方法
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}  # 初始化，prefix sum 為 0 出現過一次（空 subarray）
        currentSum = 0
        count = 0

        for num in nums:
            currentSum += num                    # 累加目前的 prefix sum
            diff = currentSum - k                # 找之前有沒有出現過這個 prefix sum
            if diff in hashmap:
                count += hashmap[diff]           # 有的話，count 加上出現次數
            if currentSum not in hashmap:
                hashmap[currentSum] = 1          # 第一次出現，初始化為