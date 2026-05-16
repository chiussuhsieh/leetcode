# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
# 難度：Medium
# 類型：Greedy

# 思路：
# 把每一跳當作一層
# 在每一跳的範圍內，找下一跳最遠能到哪（farthest）
# 當掃完這一跳的範圍（i == curEnd），就必須跳一次
# 更新 curEnd = farthest，進入下一跳的範圍

# Time: O(n)
# Space: O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0    # 下一跳最遠能到哪
        curEnd = 0      # 這一跳的邊界
        jumps = 0       # 跳了幾次

        for i in range(len(nums) - 1):  # 不需要從終點再跳，所以 -1
            farthest = max(farthest, i + nums[i])
            # 在這一跳的範圍內，持續更新下一跳最遠能到哪

            if i == curEnd:             # 掃完這一跳的範圍，必須跳一次
                jumps += 1              # 跳一次
                curEnd = farthest       # 下一跳的邊界更新成 farthest
                if curEnd >= len(nums) - 1:  # 已經能到終點，不需要再跳
                    break

        return jumps    # 回傳最少跳幾次