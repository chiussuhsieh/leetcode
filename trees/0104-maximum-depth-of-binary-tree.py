# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy
# Type: Tree / DFS Recursion

# 思路:
# 用遞迴計算左右子樹的最大深度,再組合出以 root 為根的最大深度
# 1. base case:如果 root 是 None,深度是 0
# 2. 遞迴呼叫自己拿到左子樹的最大深度 left
# 3. 遞迴呼叫自己拿到右子樹的最大深度 right
# 4. 整棵樹的最大深度 = 左右子樹中較深的那邊,再加上 root 自己這一層
# 5. 回傳 1 + max(left, right)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

# Time Complexity: O(n) — 每個節點恰好被訪問一次
# Space Complexity: O(n) — 遞迴呼叫堆疊(最壞情況樹退化成鏈狀時是 O(n))

# Pattern 筆記:
# 這題的 pattern 是「DFS 遞迴,用子問題的回傳值(數字)組合出當前節點的答案」,
# 下次看到「需要根據左右子樹算出的數值,組合出以當前節點為根的答案」的特徵就用這個方法。