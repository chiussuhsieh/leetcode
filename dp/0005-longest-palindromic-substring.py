# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# 難度：Medium
# 類型：Two Pointers（從中心往外擴展）

# 思路：
# 跟 Palindromic Substrings 一樣，從每個位置往外擴展
# 差別是這題不是數總數，而是記錄最長的回文子字串
# 每次找到更長的回文就更新 res 和 resLen

# Time: O(n²)
# Space: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""       # 記錄目前最長的回文子字串
        resLen = 0     # 記錄目前最長回文的長度

        for i in range(len(s)):    # 每個位置都當作中心試試看

            # 奇數長度回文（單個字母為中心）
            l, r = i, i            # l 和 r 從同一個位置出發
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # l >= 0：不超出左邊界
                # r < len(s)：不超出右邊界
                # s[l] == s[r]：左右兩端相同，是回文
                if (r - l + 1) > resLen:       # 如果這個回文比目前最長的還長
                    res = s[l: r + 1]           # 更新最長回文（r+1 因為 slice 不包含右邊界）
                    resLen = r - l + 1          # 更新最長長度
                l -= 1             # 往左擴展
                r += 1             # 往右擴展

            # 偶數長度回文（兩個字母為中心）
            l, r = i, i + 1       # l 和 r 從相鄰兩個位置出發
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:       # 如果這個回文比目前最長的還長
                    res = s[l: r + 1]           # 更新最長回文
                    resLen = r - l + 1          # 更新最長長度
                l -= 1             # 往左擴展
                r += 1             # 往右擴展

        return res     # 回傳最長回文子字串