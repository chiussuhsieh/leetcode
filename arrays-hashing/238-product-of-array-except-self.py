# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# 難度：Medium
# 類型：Array, Prefix Product
# 思路：
# 每個位置的答案 = 左邊所有數字的乘積 x 右邊所有數字的乘積
# 第一個 pass 從左到右，res[i] 存左邊所有數字的乘積
# 第二個 pass 從右到左，res[i] 再乘上右邊所有數字的乘積
# Pattern 筆記：
# 這題的 pattern 是「Left/Right Prefix Product」
# 第一個 pass 從左到右存左邊乘積，第二個 pass 從右到左乘上右邊乘積
# 下次看到「每個位置的答案需要左邊和右邊的累積結果」就用這個方法
# Time: O(n)
# Space: O(1)（不算 output array）

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            res[i] *= prefix          # 存左邊所有數字的乘積
            prefix *= nums[i]         # 更新 prefix
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix          # 乘上右邊所有數字的乘積
            suffix *= nums[i]         # 更新 suffix
        return res