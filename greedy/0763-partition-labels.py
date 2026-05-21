# 763. Partition Labels
# https://leetcode.com/problems/partition-labels/
# 難度：Medium
# 類型：Greedy

# 思路：
# 第一步：記錄每個字母最後出現的 index
#         dictionary 的 key 不能重複，後面的值會覆蓋前面的，自然留下最後出現的 index
# 第二步：從左到右掃，追蹤當前片段的終點
#         每掃到一個字母，更新終點 = max(end, lastIndex[c])
#         當 i == end，代表片段裡所有字母都不會再出現，切一刀！
# 跟 Jump Game II 很像：i == curEnd 時跳一次，這題 i == end 時切一刀

# Time: O(n)
# Space: O(n)

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}                     # 記錄每個字母最後出現的 index

        for i, c in enumerate(s):
            lastIndex[c] = i               # 重複的字母會覆蓋，自然留下最後出現的 index

        res = []                           # 記錄每個片段的長度
        size, end = 0, 0                   # size：目前片段的長度，end：目前片段的終點

        for i, c in enumerate(s):
            size += 1                      # 每掃一個字母，片段長度加一
            end = max(end, lastIndex[c])   # 更新片段終點：取所有掃過字母中最晚出現的 index

            if i == end:                   # 當前 index 追上片段終點
                res.append(size)           # 片段結束，記錄長度
                size = 0                   # 重置片段長度，開始新片段

        return res                         # 回傳所有片段的長度