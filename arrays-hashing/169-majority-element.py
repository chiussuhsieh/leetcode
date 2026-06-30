# 169. Majority Element
# https://leetcode.com/problems/majority-element/
# 難度：Easy
# 類型：Array, HashMap
# 思路：
# 建立 hashmap 計算每個元素出現次數
# 再 iterate hashmap.items()，同時追蹤目前最大的 count (maxCount) 和對應的 key (res)
# 每次 val 比 maxCount 大就更新 res，再更新 maxCount
# 最後回傳 res 即為出現次數最多的元素
# Pattern 筆記：
# 這題的 pattern 是「HashMap 計數 + 找最大值對應的 key」
# 下次看到「找出現次數最多/超過某個門檻的元素」就用這個方法
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1       # 第一次出現，初始化為 1
            else:
                hashmap[num] += 1      # 已存在，次數加一
        maxCount = 0
        res = 0
        for key, val in hashmap.items():
            if val > maxCount:
                res = key               # 更新目前次數最多的元素
            maxCount = max(maxCount, val)  # 更新目前最大次數
        return res