# https://leetcode.com/problems/binary-tree-right-side-view/
# Difficulty: Medium
# Type: Tree / BFS (Queue)

# 思路:
# 建立在 Level Order Traversal 的 BFS 框架上,差別是每層只收集最右邊那個節點的值
# 1. 如果 root 是 None,直接回傳空的 res
# 2. 把 root 放進 queue
# 3. 每一輪迴圈開始前,用 queueLength 固定住這一層原本的節點數量(避免受後續 append 影響)
# 4. 用 for i in range(queueLength) 跑這一層的節點
# 5. 每次 popleft 取出一個節點,如果 i 是這一層的最後一個索引(i == queueLength - 1),
#    代表這是這一層最右邊的節點,把它的值加進 res
# 6. 不論是不是最右邊,都要把它的左右子節點(如果存在)加進 queue,準備進入下一層
# 7. 回傳 res

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        res = []
        queue = collections.deque()
        if not root:
            return res
        queue.append(root)

        while queue:
            queueLength = len(queue)
            for i in range(queueLength):
                node = queue.popleft()
                if i == queueLength - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

# Time Complexity: O(n) 每個節點恰好進出 queue 一次
# Space Complexity: O(n) queue 最多同時存放一整層的節點,最寬的一層最多約 n/2 個節點

# Pattern 筆記:
# 這題的 pattern 是「BFS + 用固定住的 level 節點數量搭配索引,篩選出每層特定位置的節點」,
# 下次看到「需要按層處理,且只關心每層某個特定位置(最左/最右/第 k 個)」的特徵就用這個方法。