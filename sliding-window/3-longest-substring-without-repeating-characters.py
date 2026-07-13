# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 難度: Medium
# Type: Sliding Window (變動大小窗口)

# 思路:
# 用 left、right 兩個指針維護一個「不含重複字元」的窗口,
# 並用一個 set 記錄目前窗口內出現過的字元。
# right 指針負責逐一往右擴張窗口:
#   如果 s[right] 不在 set 裡,代表沒有重複,直接加入 set。
#   如果 s[right] 已經在 set 裡,代表窗口內有重複字元,
#   需要用 while loop 不斷從左邊移除字元(left 指針右移),
#   直到 s[right] 不再存在於 set 中為止,再把 s[right] 加入 set。
# 每一輪結束後(不論是否有重複),都用 right - left + 1 更新目前為止的最大長度。
# 這是「變動大小窗口」的經典模板:right 負責擴張,left 依情況收縮,
# 且一次可能收縮不只一格。

# Pattern 筆記:
# 這題的 pattern 是「變動大小滑動窗口 + hash set 追蹤窗口內元素」,
# 下次看到「找最長/最短連續子字串(或子陣列),且需要維持某個條件(像是不重複)」的題目,
# 就可以用「right 擴張、left 收縮」這個模板。

# Time complexity: O(n),每個字元最多被加入、移除 set 各一次
# Space complexity: O(n),最壞情況下 set 會存下整個字串的所有字元

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0  # 記錄目前為止看過的最大長度
        strSet = set()  # 用來記錄目前窗口內出現過的字元
        left = 0  # 左指針,窗口的起始位置

        for right in range(len(s)):  # 右指針逐一往右擴張窗口
            if s[right] not in strSet:  # 目前字元沒有重複
                strSet.add(s[right])  # 直接加入窗口
            else:  # 目前字元跟窗口內某個字元重複
                while s[right] in strSet:  # 持續收縮窗口,直到重複的字元被移除
                    strSet.remove(s[left])  # 移除窗口最左邊的字元
                    left += 1  # 左指針往右移動,縮小窗口
                strSet.add(s[right])  # 收縮完後,把目前字元加入窗口

            maxLength = max(maxLength, right - left + 1)  # 更新目前為止的最大長度

        return maxLength  # 回傳最終的最大長度