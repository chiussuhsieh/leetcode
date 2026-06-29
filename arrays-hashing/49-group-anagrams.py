# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# 難度：Medium
# 類型：Array, HashMap
# 思路：
# 建立空 hashmap，key 是 sorted string，value 是 anagram 的 list
# iterate array，每個字串 sorted 後 join 成 string 當 key
# 如果 key 不在 hashmap，初始化一個新 list
# 如果 key 已存在，直接 append 進去
# 最後 iterate hashmap.values() 把每個 list 加進結果 array 回傳
# Pattern 筆記：
# 這題的 pattern 是「HashMap 以 sorted string 為 key 分組」
# 下次看到「把 anagram 或有相同組成的字串分組」就用這個方法
# Time: O(n * k log k)，n 是字串數量，k 是最長字串長度
# Space: O(n)

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in range(len(strs)):
            wordKey = "".join(sorted(strs[i]))  # sorted 後 join 當 key
            if wordKey not in hashmap:
                hashmap[wordKey] = [strs[i]]    # 初始化新 list
            else:
                hashmap[wordKey].append(strs[i]) # 加進已存在的 list
        array = []
        for i in hashmap.values():
            array.append(i)                      # 每個 group 加進結果
        return array