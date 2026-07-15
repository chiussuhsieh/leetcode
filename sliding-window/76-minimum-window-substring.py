# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
# 難度: Hard
# Type: Sliding Window (變動大小窗口,找最短)

# 思路:
# 用 tMap 記錄 t 每個字元的次數,windowMap 記錄窗口內每個字元的次數,
# matches 記錄目前有幾種字元的次數已經達到(>=)tMap 對應字元的要求。
# right 指針每輪把 s[right] 加入 windowMap,
# 若該字元在 tMap 裡且加入後次數剛好等於 tMap 對應次數,matches += 1。
# 當 matches == len(tMap)(窗口已涵蓋 t 所有字元),進入 while 持續收縮:
#   若目前窗口長度比記錄的 minLength 還短,才同時更新 minLength 和 resultLeft,
#   若 s[left] 在 tMap 裡且移除前次數剛好等於 tMap 要求,matches -= 1,
#   不論是否在 tMap,windowMap[s[left]] 都要減一,left 右移一格。
# 最後用 resultLeft 和 minLength 切出答案子字串,若從未涵蓋過則回傳空字串。

# Pattern 筆記:
# 這題的 pattern 是「變動大小滑動窗口 + 頻率表 + matches 計數器,找最短涵蓋窗口」,
# 下次看到「找最短子字串/子陣列,涵蓋另一個集合所有元素(次數 >= 要求即可)」的題目,
# 就可以用這個模板:加入時次數達標才 +1,移除時次數跌破才 -1,達標時用 while 收縮並記錄最小值。
# 特別注意:記錄「最短長度」跟「對應的起始位置」這兩個變數,必須綁在同一個 if 條件裡一起更新,
# 不能其中一個用 min() 無條件比較、另一個獨立無條件覆寫,否則兩者會對不上。

# Time complexity: O(m + n),m=len(t), n=len(s),每個字元最多被加入、移除各一次
# Space complexity: O(m + n),tMap 最多存 t 的所有不同字元,windowMap 最多存 s 的所有不同字元

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLength = float("inf")  # 記錄目前為止看過的最短合法窗口長度
        resultLeft = 0  # 記錄目前最短窗口對應的 left 位置
        left = 0  # 左指針,窗口的起始位置
        tMap = Counter(t)  # 記錄 t 裡每個字元出現的次數
        windowMap = {}  # 記錄窗口內每個字元出現的次數
        matches = 0  # 記錄目前有幾種字元的次數已經達到 tMap 對應字元的要求

        for right in range(len(s)):  # 右指針逐一往右擴張窗口
            if s[right] not in windowMap:  # 這個字元還沒出現過
                windowMap[s[right]] = 1  # 初始化次數為 1
            else:
                windowMap[s[right]] += 1  # 已經出現過,次數加一

            if s[right] in tMap:  # 只有 t 裡有的字元才需要更新 matches
                if windowMap[s[right]] == tMap[s[right]]:  # 加入後次數剛好達到 tMap 要求
                    matches += 1  # 這個字元新達成 match

            while matches == len(tMap):  # 窗口已經涵蓋 t 的所有字元,持續收縮找更短的窗口
                if right - left + 1 < minLength:  # 只有窗口真的比目前紀錄還短時
                    minLength = right - left + 1  # 才更新最短長度
                    resultLeft = left  # 同時更新對應的 left 位置

                if s[left] in tMap:  # 只有 t 裡有的字元才需要更新 matches
                    if windowMap[s[left]] == tMap[s[left]]:  # 移除前次數剛好等於 tMap 要求
                        matches -= 1  # 移除後次數會跌破要求,match 被打破

                windowMap[s[left]] -= 1  # 不論是否在 tMap,都移除最左邊字元,次數減一
                left += 1  # 左指針往右移動,縮小窗口

        return s[resultLeft: resultLeft + minLength] if minLength != float("inf") else ""  # 切出答案子字串,找不到就回傳空字串