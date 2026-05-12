# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/
# 難度：Medium
# 類型：Two Pointers（從中心往外擴展）

# 思路：
# 每個位置都當作回文的中心，往外擴展
# 回文有兩種：奇數長度（單個字母為中心）和偶數長度（兩個字母為中心）
# 兩種都試，res 累加所有找到的回文數量

# Time: O(n²)
# Space: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0                              # 記錄回文子字串的總數

        for i in range(len(s)):              # 每個位置都當作中心試試看

            # 奇數長度回文（單個字母為中心）
            l, r = i, i                      # l 和 r 從同一個位置出發
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # l >= 0：不超出左邊界
                # r < len(s)：不超出右邊界
                # s[l] == s[r]：左右兩端相同，是回文
                res += 1                     # 找到一個回文
                l -= 1                       # 往左擴展
                r += 1                       # 往右擴展

            # 偶數長度回文（兩個字母為中心）
            l, r = i, i + 1                  # l 和 r 從相鄰兩個位置出發
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1                     # 找到一個回文
                l -= 1                       # 往左擴展
                r += 1                       # 往右擴展

        return res                           # 所有回文子字串的總數