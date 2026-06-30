# 706. Design HashMap
# https://leetcode.com/problems/design-hashmap/
# 難度：Easy
# 類型：Array, HashMap
# 思路：
# 初始化一個大小 10^6 + 1 的 array，全部設成 -1，index 就是 key
# put(key, value) → array[key] 設成 value
# get(key) → 直接回傳 array[key]，不存在就是 -1
# remove(key) → array[key] 設回 -1，等於假裝這個 key 不存在
# Pattern 筆記：
# 這題的 pattern 是「Array 模擬 HashMap」
# 下次看到「key 範圍固定、需要 O(1) get/put/remove」就用這個方法
# Time: O(1) for all operations
# Space: O(n)，n = 10^6 + 1

class MyHashMap:

    def __init__(self):
        self.array = [-1] * (10 ** 6 + 1)  # index 代表 key，初始全為 -1

    def put(self, key: int, value: int) -> None:
        self.array[key] = value             # 設定/更新 value

    def get(self, key: int) -> int:
        return self.array[key]              # 回傳 value，不存在即 -1

    def remove(self, key: int) -> None:
        self.array[key] = -1                # 移除等於設回 -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)