# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# 難度：Medium
# 類型：Array, HashMap, Heap
# 思路：
# 建立 hashmap 計算每個元素出現次數
# 把 (-count, num) 全部 push 進 heap，用負數模擬 max-heap
# while k 次，每次 pop 出目前最大的，取出 num 加進 res
# 最後回傳 res
# Pattern 筆記：
# 這題的 pattern 是「HashMap 計數 + Max-Heap 取前 k 大」
# 下次看到「找出現頻率/數值前 k 高（或低）的元素」就用這個方法
# Python heapq 是 min-heap，取負數模擬 max-heap
# Time: O(n log n)
# Space: O(n)

import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1            # 第一次出現，初始化為 1
            else:
                hashmap[num] += 1           # 已存在，次數加一
        maxHeap = []
        for key, val in hashmap.items():
            heapq.heappush(maxHeap, (-val, key))  # 負數模擬 max-heap
        res = []
        while k:
            ans = heapq.heappop(maxHeap)    # pop 出目前次數最大的
            res.append(ans[1])              # 取出原始數字
            k -= 1
        return res