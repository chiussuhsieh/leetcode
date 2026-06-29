# 705. Design HashSet
# https://leetcode.com/problems/design-hashset/
# 難度：Easy
# 類型：Array, HashSet
# 思路：
# 初始化一個大小 10^6 + 1 的 boolean array，index 就是 key
# add(key) → data[key] 設成 True
# remove(key) → data[key] 設成 False
# contains(key) → 直接回傳 data[key]
# Pattern 筆記：
# 這題的 pattern 是「Boolean Array 模擬 HashSet」
# 下次看到「key 範圍固定、需要 O(1) 查找」就用這個方法
# Time: O(1) for all operations
# Space: O(n)，n = 10^6 + 1

class MyHashSet:

    def __init__(self):
        self.data = [False] * (10 ** 6 + 1)  # index 代表 key，初始全為 False

    def add(self, key: int) -> None:
        self.data[key] = True                 # 標記為存在

    def remove(self, key: int) -> None:
        self.data[key] = False                # 標記為不存在

    def contains(self, key: int) -> bool:
        return self.data[key]                 # 直接回傳是否存在