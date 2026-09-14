# 0146. LRU Cache
# https://leetcode.com/problems/lru-cache/
# 難度：Medium
# 類型：Linked List（Design，經典大廠面試題）

# 思路：
# 需要同時做到「O(1) 查詢某個 key」和「O(1) 找到並移除最久沒使用的 key、
# O(1) 把某個 key 標記為最近使用」，單靠 hashmap 無法維護使用順序，
# 單靠 linked list 無法 O(1) 定位特定 key。解法是組合兩者：
# hashmap（key -> 節點物件，O(1) 查詢）+ 雙向鏈結串列（維護使用順序，
# O(1) 在任意位置插入/刪除）。
#
# 雙向鏈結串列用兩個哨兵節點（self.left、self.right）固定頭尾，讓「串列是
# 空的」「只有一個節點」等邊界情況都能用同一套邏輯處理，不需特殊判斷。
# 串列排列方式：最舊的節點緊接在 self.left 後面（self.left.next），
# 最新使用過的節點緊接在 self.right 前面（self.right.prev）。
#
# 兩個輔助方法：
# - remove(node)：讓 node 前後兩個節點直接相連，跳過 node
#   （node.prev.next = node.next，node.next.prev = node.prev）。
# - insert(node)：把 node 插入到 self.right 前面（最新端）
#   （四條連接關係，順序上要先用 self.right.prev 抓到「舊的最新節點」，
#   最後才更新 self.right.prev = node，避免先改了再用抓不到舊值）。
#
# get(key)：key 不存在回傳 -1；存在的話，把該節點 remove 再 insert
# （移到最新端），回傳 node.value。
#
# put(key, value)：key 已存在則更新 node.value，並 remove+insert 移到
# 最新端。key 不存在則建立新 Node、存進 cache、insert 到最新端；插入後
# 若 len(cache) > capacity，代表超過容量，取出最舊節點（self.left.next）
# 移除，同時要用 oldNode.key（而非傳入的 key）從 hashmap 中刪除對應項目
# ——這是容易搞混的地方，要刪除的 key 是「最舊節點自己的 key」，不是
# 這次呼叫 put 傳進來的 key。

# Pattern 筆記：
# 這是「hashmap + 雙向鏈結串列」的經典 pattern，核心價值是用 hashmap 換取
# O(1) 定位、用雙向鏈結串列換取 O(1) 的任意位置插入/刪除（不需要像單向
# linked list 或陣列那樣搬移或線性尋找前一個節點）。
# 用兩個哨兵節點消除邊界判斷，是這整個章節反覆出現的設計哲學的延伸：
# 從 dummy node（單向）到這裡的雙哨兵（雙向），本質上都是「讓操作對象
# 永遠有前後可依靠，不需要特殊處理頭尾」。
# 這個 pattern 直接延伸到 LFU Cache（下一題），只是要額外維護「使用頻率」
# 這個維度。

# Time complexity: get、put 皆為 O(1)
# Space complexity: O(capacity)，hashmap 與鏈結串列最多各存 capacity 個節點

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        self.left = Node(0, 0)   # 哨兵，左邊固定代表「最舊端之前」
        self.right = Node(0, 0)  # 哨兵，右邊固定代表「最新端之後」
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # 讓 node 前後兩個節點直接相連，跳過 node
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        # 插入到 self.right 前面（最新端）
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)   # 標記為最近使用：先摘除
        self.insert(node)   # 再插入到最新端
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
            if len(self.cache) > self.capacity:
                oldNode = self.left.next  # 最舊的節點
                self.remove(oldNode)
                self.cache.pop(oldNode.key)  # 用最舊節點自己的 key 刪除，不是傳入的 key