# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# 難度：Easy
# 類型：Array, HashMap
# 思路：
# 先比長度，不一樣直接 return False
# 建立 sMap 記錄 s 每個字母出現次數
# iterate t，每個字母在 sMap 對應次數 -= 1
# 如果字母不在 sMap 直接 return False
# 最後檢查 sMap 所有 value 是否都為 0
# Pattern 筆記：
# 這題的 pattern 是「HashMap 計數比對」
# 下次看到「兩個字串/陣列的元素組成是否相同」就用這個方法
# Time: O(n)
# Space: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):               # 長度不同直接排除
            return False
        sMap = {}
        for character in s:
            if character in sMap:
                sMap[character] += 1       # 已存在，次數加一
            else:
                sMap[character] = 1        # 第一次出現，初始化為 1
        for character in t:
            if character not in sMap:
                return False               # t 有 s 沒有的字母
            else:
                sMap[character] -= 1       # 找到對應字母，次數減一
        for v in sMap.values():
            if v != 0:
                return False               # 有字母次數不為 0，不是 anagram
        return True