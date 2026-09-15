# 0460. LFU Cache
# https://leetcode.com/problems/lfu-cache/
# 難度：Hard
# 類型：Linked List（Design，LRU Cache 的進階版）

# 思路：
# 淘汰規則從「最久沒被使用」改成「使用頻率最低，頻率打平則淘汰其中最久沒被
# 使用的」。單一條雙向鏈結串列（像 LRU 那樣）只能回答「誰最久沒被用」，
# 無法同時回答「誰的頻率最低」，兩個維度混在一起難以查詢。
#
# 解法：把「相同頻率」的 key 各自分成一群，每一群自己維護一條獨立的雙向
# 鏈結串列（群內部用 LRU 的邏輯排序：最新使用的在右端、最久沒用的在左端）。
# 用 self.freqMap（頻率 -> DLinkedList）查到某個頻率對應的串列；
# 用 self.cache（key -> node）查到某個 key 對應的節點；
# 用 self.minFreq 追蹤目前最小頻率，避免每次都要掃描找最小值。
#
# minFreq 的更新邏輯（關鍵推導）：
# - 新插入一個 key，頻率固定是 1，一定是當下最小，所以 minFreq 直接設為 1。
# - 一個 key 的頻率增加（f -> f+1），不會讓 minFreq 變小（其他 key 都沒動，
#   原本更小的頻率依然存在；就算它自己是最小的，變大後 minFreq 只會不變
#   或變大）。
# - 若 f 剛好等於 minFreq，且 f 這條串列因為這次移動而變空，代表「所有
#   頻率為 f 的 key」都不存在了，因為 f 曾是最小值（沒有比它更小的），
#   現在 f 空了，且這個 key 自己佔據了 f+1，可以直接斷定新的 minFreq 就是
#   f+1，不需要重新掃描確認。
#
# 節點（Node）比 LRU 多存一個 freq 屬性，因為要知道「這個節點目前屬於
# 哪一條頻率串列」，才能在頻率變動時，用 self.freqMap[node.freq] 找到
# 它原本所在的串列並移除。
#
# DLinkedList 是抽出來的獨立 class，把 LRU 裡「左右哨兵 + remove + insert」
# 的邏輯封裝起來，讓每個頻率都能各自擁有一份獨立的串列實例；額外維護
# self.size 記錄節點數，用來判斷串列是否變空（觸發 minFreq 更新的關鍵依據）。
#
# get(key)：key 不存在回傳 -1。存在的話：從 node.freq 對應的串列移除該
# 節點；若移除後串列變空且該頻率等於 minFreq，minFreq += 1；node.freq
# 本身 +1；若新頻率的串列不存在就新建；把節點插入新頻率的串列；回傳
# node.value。
#
# put(key, value)：capacity 為 0 時直接 return（不做任何事）。若 key 已
# 存在，更新 value，並直接呼叫 self.get(key) 借用其「頻率更新、換串列」
# 的邏輯，避免整段複製貼上。若 key 不存在：先檢查加入後是否超過容量，
# 若會超過，從 minFreq 對應的串列中找出最舊節點（minLinkedList.left.next）
# 淘汰（從串列移除、從 cache 刪除，注意要用「被淘汰節點自己的 key」
# 而不是本次 put 傳入的 key）；接著不論容量是否原本已滿，都要建立新節點
# （freq=1）、存入 cache、插入 freqMap[1]（不存在則新建）、並將 minFreq
# 設為 1（新 key 必定是當下最小頻率）。

# Pattern 筆記：
# 這題是 LRU Cache 的直接延伸：把 LRU 的「hashmap + 雙向鏈結串列」模式
# 升級成「hashmap（key）+ hashmap（頻率）+ 多條雙向鏈結串列」，用一個
# 額外維度（頻率）分桶，每一桶內部繼續沿用 LRU 的排序邏輯。這種「分桶 +
# 桶內用已知結構排序」的思路，遇到多維度排序需求時可以優先考慮。
# 把 LRU 的左右哨兵邏輯抽成獨立的 DLinkedList class 是關鍵重構，讓同一套
# 邏輯可以被實例化很多份，這也是物件導向設計中「封裝可重複使用的行為」
# 的典型範例。
# minFreq 的更新完全靠邏輯推導而非重新掃描，是這題效能的關鍵，體現了
# 「善用已知的不變量（invariant）減少計算」這個更廣泛的演算法設計原則。

# Time complexity: get、put 皆為 O(1)
# Space complexity: O(capacity)


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1  # 新建立的節點，使用頻率從 1 開始
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self.left = Node(0, 0)   # 哨兵，代表「最舊端之前」
        self.right = Node(0, 0)  # 哨兵，代表「最新端之後」
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0  # 這條串列目前的真實節點數

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node
        self.size += 1


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}     # key -> node
        self.freqMap = {}   # freq -> DLinkedList
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        linkedList = self.freqMap[node.freq]
        linkedList.remove(node)
        # 該頻率串列變空、且該頻率正好是目前最小頻率 -> 最小頻率必然變成 freq+1
        if linkedList.size == 0 and node.freq == self.minFreq:
            self.minFreq += 1
        node.freq += 1
        if node.freq not in self.freqMap:
            self.freqMap[node.freq] = DLinkedList()
        newLinkedList = self.freqMap[node.freq]
        newLinkedList.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.get(key)  # 借用 get 的邏輯完成頻率更新與換串列
        else:
            if len(self.cache) + 1 > self.capacity:
                # 從最小頻率的串列中淘汰最舊的節點
                minLinkedList = self.freqMap[self.minFreq]
                deleteNode = minLinkedList.left.next
                minLinkedList.remove(deleteNode)
                del self.cache[deleteNode.key]  # 用被淘汰節點自己的 key，不是傳入的 key

            newNode = Node(key, value)
            self.cache[key] = newNode
            if 1 not in self.freqMap:
                self.freqMap[1] = DLinkedList()
            self.freqMap[1].insert(newNode)
            self.minFreq = 1  # 新 key 頻率固定是 1，必定是當下最小