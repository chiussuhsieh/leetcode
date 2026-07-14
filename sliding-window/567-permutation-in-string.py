# 567. Permutation In String
# https://leetcode.com/problems/permutation-in-string/
# 難度: Medium
# Type: Sliding Window (固定大小窗口)

# 思路:
# 用 s1Map 記錄 s1 每個字母的次數,windowMap 記錄窗口內每個字母的次數,
# matches 記錄目前有幾種字母的次數跟 s1Map 對應字母的次數完全相等。
# right 指針每輪把 s2[right] 加入 windowMap,
# 若該字元在 s1Map 裡,比較加入後次數:
#   剛好等於 s1Map 對應次數 → matches += 1
#   等於 s1Map 對應次數 + 1(從相等變超過) → matches -= 1
# 當窗口大小(right - left + 1)超過 len(s1) 時,收縮窗口:
#   若 s2[left] 在 s1Map 裡,先比較移除前次數:
#     剛好等於 s1Map 對應次數 → matches -= 1
#     等於 s1Map 對應次數 + 1(超過變回相等) → matches += 1
#   接著不論是否在 s1Map,都把 windowMap[s2[left]] 次數減一,left 右移一格。
# 每輪檢查 matches == len(s1Map),相等就回傳 True。

# Pattern 筆記:
# 這題的 pattern 是「固定大小滑動窗口 + 頻率表 + matches 計數器」,
# 下次看到「判斷窗口是否為另一個字串的排列(anagram)」的題目,
# 就可以用「加入/移除時比較次數轉變,更新 matches」這個技巧,
# 避免每次都重新比較整個 hashmap。

# Time complexity: O(n),n 是 s2 的長度,每個字元最多被加入、移除各一次
# Space complexity: O(1),因為只包含小寫英文字母,hashmap 最多存 26 個 key,是常數大小

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):  # s1 比 s2 還長,不可能存在排列,直接回傳 False
            return False

        s1Map = Counter(s1)  # 記錄 s1 裡每個字母出現的次數
        left = 0  # 左指針,窗口的起始位置
        windowMap = {}  # 記錄窗口內每個字母出現的次數
        matches = 0  # 記錄目前有幾種字母的次數,跟 s1Map 對應字母的次數完全相等

        for right in range(len(s2)):  # 右指針逐一往右擴張窗口
            if s2[right] not in windowMap:  # 這個字母還沒出現過
                windowMap[s2[right]] = 1  # 初始化次數為 1
            else:
                windowMap[s2[right]] += 1  # 已經出現過,次數加一

            if s2[right] in s1Map:  # 只有 s1 裡有的字母才需要更新 matches
                if windowMap[s2[right]] == s1Map[s2[right]]:  # 加入後次數剛好變成相等
                    matches += 1  # 這個字母新達成 match
                elif windowMap[s2[right]] == s1Map[s2[right]] + 1:  # 加入後次數從相等變成超過一個
                    matches -= 1  # 這個字母原本 match,現在破功了

            if right - left + 1 > len(s1):  # 窗口大小超過 s1 長度,需要收縮
                if s2[left] in s1Map:  # 只有 s1 裡有的字母才需要更新 matches
                    if windowMap[s2[left]] == s1Map[s2[left]]:  # 移除前次數剛好相等
                        matches -= 1  # 移除後次數變少,match 被打破
                    elif windowMap[s2[left]] == s1Map[s2[left]] + 1:  # 移除前次數是相等值加一(超過一個)
                        matches += 1  # 移除後次數剛好變回相等,重新達成 match

                windowMap[s2[left]] -= 1  # 不論是否在 s1Map,都移除最左邊字母,次數減一
                left += 1  # 左指針往右移動,縮小窗口

            if matches == len(s1Map):  # 窗口內每種字母的次數都跟 s1 完全相等
                return True  # 找到排列了

        return False  # 走完整個 s2 都沒找到符合條件的窗口