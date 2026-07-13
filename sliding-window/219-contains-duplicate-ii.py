# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/
# 難度: Easy
# Type: Sliding Window (固定大小窗口)

# 思路:
# 用 left、right 兩個指針維護一個大小固定為 k+1 的窗口,
# 並用一個 set 記錄目前窗口內出現過的數字。
# right 指針負責往右擴張窗口:
#   先檢查 nums[right] 是否已經存在於 set 中,
#   如果存在,代表窗口內(也就是 abs(i-j) <= k 的範圍內)已經有重複值,直接回傳 True。
#   如果不存在,把 nums[right] 加入 set,並讓 right 往右移動一格。
# 每次擴張後檢查窗口大小(right - left)是否超過 k,
# 如果超過,代表窗口太大了,需要把最左邊的元素從 set 中移除,
# 再讓 left 往右移動一格,縮小窗口回到合法大小。
# 這樣可以確保窗口內任兩個索引的差距永遠不超過 k。

# Pattern 筆記:
# 這題的 pattern 是「固定大小滑動窗口 + hash set 檢查重複」,
# 下次看到「索引距離限制在 k 以內」或「固定區間大小」的題目,
# 且需要快速判斷區間內是否有重複值時,就可以用這個方法。

# Time complexity: O(n),每個元素最多被加入、移除 set 各一次
# Space complexity: O(min(n, k+1)),set 最多同時存放 k+1 個元素

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, right = 0, 0  # 初始化左右指針,窗口從第 0 個元素開始
        numSet = set()  # 用來記錄目前窗口內出現過的數字

        while right < len(nums):  # 右指針持續往右擴張,直到走完整個陣列
            if nums[right] not in numSet:  # 檢查目前數字是否已經在窗口內出現過
                numSet.add(nums[right])  # 沒出現過,加入 set
                right += 1  # 右指針往右擴張窗口

                if right - left > k:  # 檢查窗口大小是否超過合法範圍(k+1)
                    numSet.remove(nums[left])  # 移除窗口最左邊的元素
                    left += 1  # 左指針往右移動,縮小窗口
            else:
                return True  # 發現重複值,且距離在 k 以內,直接回傳 True

        return False  # 走完整個陣列都沒找到符合條件的重複值