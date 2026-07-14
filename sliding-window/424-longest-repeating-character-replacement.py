# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/
# 難度: Medium
# Type: Sliding Window (變動大小窗口)

# 思路:
# 用 left、right 指針維護窗口,hashmap(sMap)記錄窗口內每個字母出現的次數。
# right 指針每輪往右擴張,更新 sMap 裡對應字母的次數,
# 並用 maxFreq 記錄目前為止看過最大的字母出現次數。
# 判斷 windowSize(right - left + 1)減去 maxFreq 是否超過 k,
# 若超過(isValid=False),就把 sMap[s[left]] 次數減一,left 右移一格。
# 每輪結束後用 max(right - left + 1, longest) 更新答案。

# Pattern 筆記:
# 這題的 pattern 是「變動大小滑動窗口 + 頻率表 + 只增不減的歷史最大值」,
# 下次看到「窗口合法性取決於某個歷史最大值(次數、總和等),
# 且窗口大小本身單調不減」的題目,就可以用「只移動一格、不用 while 收縮」這個技巧。

# Time complexity: O(n),每個字元只會被 right 指針走訪一次
# Space complexity: O(1),因為只包含大寫英文字母,hashmap 最多存 26 個 key,是常數大小

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0  # 記錄目前為止看過的最大合法窗口長度
        maxFreq = 0  # 記錄窗口內「歷史上出現過」的最大字母次數(只增不減)
        sMap = {}  # 記錄窗口內每個字母出現的次數
        left = 0  # 左指針,窗口的起始位置

        for right in range(len(s)):  # 右指針逐一往右擴張窗口
            if s[right] not in sMap:  # 這個字母還沒出現過
                sMap[s[right]] = 1  # 初始化次數為 1
            else:
                sMap[s[right]] += 1  # 已經出現過,次數加一

            maxFreq = max(maxFreq, sMap[s[right]])  # 更新歷史最大次數

            isValid = right - left + 1 - maxFreq <= k  # 判斷目前窗口是否合法(需要替換的字元數 <= k)

            if not isValid:  # 窗口不合法
                sMap[s[left]] -= 1  # 把最左邊的字母次數減一
                left += 1  # 左指針往右移動一格,窗口打平(大小不變)

            longest = max(right - left + 1, longest)  # 更新目前為止的最大合法窗口長度

        return longest  # 回傳最終答案