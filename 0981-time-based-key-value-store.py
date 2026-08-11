# 0981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/
# 難度：Medium
# 類型：Binary Search

# 思路：
# 用 dictionary（self.store）存放每個 key 對應的歷史紀錄，value 是一個 list，
# 裡面存著這個 key 曾經被 set 過的所有 (value, timestamp)，依照 set 呼叫順序存入。
# 因為題目保證每次 set 的 timestamp 嚴格遞增，這個 list 天生就是依照 timestamp 遞增排序的，
# 這個特性讓 get 可以用 binary search 來查詢。
#
# set(key, value, timestamp)：
# 如果 key 不存在，先建立空 list，接著不管 key 存不存在，都把 (value, timestamp) append 進去。
#
# get(key, timestamp)：
# 先判斷 key 是否存在，不存在直接回傳空字串（因為完全沒有這個 key 的紀錄）。
# 否則在 self.store[key] 這個 list 上做 binary search，left 設 0，right 設 len-1。
# 每一輪比較 middle 位置的 timestamp 跟查詢的 timestamp：
#   如果 middle 的 timestamp <= 查詢的 timestamp，代表這筆紀錄有可能是答案，但可能還有更接近的，
#   left 移到 middle + 1，繼續往右找。
#   否則代表這筆紀錄太新了，不可能是答案，right 移到 middle - 1。
# 迴圈結束後，left 停在「第一個 timestamp 大於查詢值的位置」，答案落在 left 的前一個位置，
# 也就是 right（因為迴圈結束時 left = right + 1，兩者等價）。
# 如果 right < 0，代表這個 key 裡沒有任何一筆紀錄的 timestamp <= 查詢值，回傳空字串；
# 否則回傳 self.store[key][right][0]（也就是 value）。

# Pattern 筆記：
# 這題的 pattern 是「在遞增排序的 list 上找小於等於目標值的最新一筆」，
# 下次看到「歷史紀錄依時間嚴格遞增 + 查詢某時間點之前最新的狀態」的特徵就用這個方法，
# 邏輯延伸自 0035 Search Insert Position（找不到時 left 停在插入點，答案在 left - 1 / right）。

# Time complexity: set() O(1)，get() O(log n)，n 為該 key 的紀錄筆數
# Space complexity: O(n)，n 為所有 set 呼叫的總筆數

class TimeMap:

    def __init__(self):
        self.store = {}  # key -> [(value, timestamp), ...]，依 timestamp 遞增排序

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:  # key 第一次出現，先建立空 list
            self.store[key] = []
        self.store[key].append((value, timestamp))  # 把新紀錄存進去

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:  # 這個 key 從來沒被 set 過
            return ""
        left = 0  # 搜尋範圍的左邊界
        right = len(self.store[key]) - 1  # 搜尋範圍的右邊界
        while left <= right:  # 左右邊界還沒交叉就繼續找
            middle = (left + right) // 2  # 取中間 index
            if self.store[key][middle][1] <= timestamp:  # 這筆紀錄的時間符合條件
                left = middle + 1  # 繼續往右找有沒有更接近的
            else:  # 這筆紀錄太新了，不符合條件
                right = middle - 1
        return self.store[key][right][0] if right >= 0 else ""  # right < 0 代表沒有符合條件的紀錄