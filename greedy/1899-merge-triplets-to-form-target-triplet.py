# 1899. Merge Triplets to Form Target Triplet
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
# 難度：Medium
# 類型：Greedy

# 思路：
# 關鍵觀察：如果一個 triplet 的任何一個值超過 target 對應的值，不能用！
# 因為合併取最大值，用了它會讓結果超過 target
# 只合併每個值都 <= target 的 triplet
# 最後看合併結果是不是等於 target

# Time: O(n)
# Space: O(1)

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]                    # 記錄合併後的結果，初始化成 [0,0,0]

        for t in triplets:                 # 遍歷每個 triplet
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                # 每個值都不超過 target 對應的值，這個 triplet 可以用
                # 超過的話合併後會讓結果超過 target，不能用

                res[0] = max(res[0], t[0]) # 合併：取每個位置的最大值
                res[1] = max(res[1], t[1])
                res[2] = max(res[2], t[2])

        return res == target               # 合併結果是不是等於 target