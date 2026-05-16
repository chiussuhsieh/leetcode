# 55. Jump Game
# https://leetcode.com/problems/jump-game/
# 難度：Medium
# 類型：Greedy

# 思路：
# 追蹤「目前歷史上能到達的最遠位置」maxReach
# 每個位置更新 maxReach = max(maxReach, i + nums[i])
# 如果某個位置 i > maxReach，代表這個位置根本不可能被到達
# 如果 loop 跑完都沒有卡住，代表能到終點

# Time: O(n)
# Space: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0       # 記錄歷史上能到達的最遠 index

        for i in range(len(nums)):   # 從左到右檢查每個位置
            if i > maxReach:
                return False         # i 超過最遠能到的位置，代表到不了這裡
            
            maxReach = max(maxReach, i + nums[i])
            # i + nums[i]：從 index i 最遠能跳到哪
            # max：保留歷史上能到的最遠位置

        return True        # loop 跑完都沒卡住，代表能到終點