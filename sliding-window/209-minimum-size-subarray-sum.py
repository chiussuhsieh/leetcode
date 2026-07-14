# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# 難度: Medium
# Type: Sliding Window (變動大小窗口,找最短)

# 思路:
# 用 left、right 指針維護窗口,windowSum 累加窗口內元素總和。
# right 指針每輪把 nums[right] 加入 windowSum。
# 只要 windowSum >= target(窗口合法),就用 while loop 持續收縮左邊:
#   先用目前窗口大小(right - left + 1)更新 minLength,
#   再把 nums[left] 從 windowSum 移除,left 右移一格,
#   直到 windowSum 小於 target 為止(窗口不再合法,跳出 while)。
# 最終回傳 minLength(如果從未達標則為 inf,需轉換成 0)。

# Pattern 筆記:
# 這題的 pattern 是「變動大小滑動窗口,找最短合法子陣列」,
# 下次看到「總和/數量達到門檻,求最短連續區間」的題目,
# 就可以用「right 擴張、達標時用 while 持續收縮並記錄最小值」這個模板,
# 跟找最長時「right 擴張、不合法時收縮」的方向剛好相反。

# Time complexity: O(n),每個元素最多被加入、移除各一次
# Space complexity: O(1),只用了固定的幾個變數

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0  # 左指針,窗口的起始位置
        minLength = float("inf")  # 記錄目前為止看過的最短合法窗口長度
        windowSum = 0  # 窗口內元素的總和

        for right in range(len(nums)):  # 右指針逐一往右擴張窗口
            windowSum += nums[right]  # 把新元素加入窗口總和

            while windowSum >= target:  # 只要窗口總和達標,就持續收縮
                minLength = min(right - left + 1, minLength)  # 記錄目前合法窗口的大小
                windowSum -= nums[left]  # 移除最左邊元素
                left += 1  # 左指針往右移動,縮小窗口

        return minLength if minLength != float("inf") else 0  # 如果從未達標,回傳 0;否則回傳最短長度