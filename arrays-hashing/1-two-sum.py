# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# 難度：Easy
# 類型：Array, HashMap
# 思路：
# 建立空 hashmap，iterate array
# 每次先算 complement = target - nums[i]
# 如果 complement 在 hashmap 裡，找到答案，回傳兩個 index
# 如果不在，把 nums[i] 和它的 index 存進 hashmap
# 邊查邊存確保不會和自己配對
# Pattern 筆記：
# 這題的 pattern 是「HashMap 邊查邊存」
# 下次看到「找兩個數字的關係（相加、相差）並回傳 index」就用這個方法
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:          # 找到配對
                return (i, hashmap[complement])
            else:
                hashmap[nums[i]] = i           # 存入當前數字和 index