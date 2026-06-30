# 229. Majority Element II
# https://leetcode.com/problems/majority-element-ii/
# 難度：Medium
# 類型：Array, HashMap
# 思路：
# 建立 hashmap 計算每個元素出現次數
# 算出門檻 majority = len(nums) / 3
# iterate hashmap.items()，count 超過門檻的元素加進 res
# 最後回傳 res
# Pattern 筆記：
# 這題的 pattern 是「HashMap 計數 + 篩選超過門檻的元素」
# 跟 Majority Element 類似，差別是門檻變 n/3，且可能有多個答案，用 array 收集
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = len(nums) / 3
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1       # 第一次出現，初始化為 1
            else:
                hashmap[num] += 1      # 已存在，次數加一
        res = []
        for key, val in hashmap.items():
            if val > majority:
                res.append(key)        # 超過門檻，加進結果
        return res