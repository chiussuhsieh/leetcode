# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Difficulty: Medium
# Type: Tree / BFS (Queue)

# 思路:
# 用 queue 做 BFS,一層一層處理,每層的節點值收集成一個 list
# 1. 如果 root 是 None,直接回傳空的 res
# 2. 把 root 放進 queue
# 3. 只要 queue 不是空的就繼續:先建立空的 level list 來裝這一層的值
# 4. 用 for i in range(len(queue)) 跑這一層的節點數量(range 只在開始時計算一次長度,
#    所以之後加進 queue 的下一層節點不會影響這一層的迭代次數)
# 5. 每次 popleft 取出一個節點,把它的值加進 level
# 6. 如果它有左子節點就 append 進 queue,有右子節點也 append 進 queue
# 7. 這一層處理完之後,把 level 加進 res
# 8. 回傳 res

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        queue = collections.deque()
        res = []
        if not root:
            return res
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                element = queue.popleft()
                level.append(element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            res.append(level)
        return res

# Time Complexity: O(n) 每個節點恰好進出 queue 一次
# Space Complexity: O(n) queue 最多同時存放一整層的節點,最寬的一層最多約 n/2 個節點,加上 res 也是 O(n)

# Pattern 筆記:
# 這題的 pattern 是「BFS + 用 len(queue) 切出每一層」,
# 下次看到「需要按層處理節點、或每層要分開統計」的特徵就用這個方法。