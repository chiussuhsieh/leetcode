# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# 難度：Easy
# 類型：Array, String
# 思路：
# 先把第一個字串當作 prefix
# iterate 剩下的字串，如果當前字串開頭不符合 prefix
# 就一直砍掉 prefix 最後一個字母直到符合為止
# 最後回傳 prefix，如果是空字串回傳 ""
# Pattern 筆記：
# 這題的 pattern 是「逐步縮短 prefix 匹配」
# 下次看到「找所有字串的公共前綴」就用這個方法
# 先用第一個字串當 prefix，不符合就從後面砍，直到所有字串都符合
# Time: O(n * m)，n 是字串數量，m 是最短字串長度
# Space: O(1)

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i][:len(prefix)] != prefix:  # 開頭不符合就一直砍
                prefix = prefix[:-1]                 # 砍掉最後一個字母
        return prefix if prefix else ""              # 空字串回傳 ""