# https://leetcode.com/problems/invert-binary-tree/
# Difficulty: Easy
# Type: Tree / DFS Recursion

# 思路:
# 用遞迴翻轉整棵樹,每個節點都要交換左右子樹
# 1. base case:如果 root 是 None,回傳 None
# 2. 用 tmp 暫存 root.left,避免交換時遺失原本的左子樹指標
# 3. root.left 指向原本的 root.right
# 4. root.right 指向 tmp(也就是原本的 root.left)
# 5. 對交換後的 root.left 和 root.right 分別遞迴呼叫,讓子樹內部也翻轉
# 6. 回傳 root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Time Complexity: O(n) — 每個節點恰好被訪問一次
# Space Complexity: O(n) — 遞迴呼叫堆疊(最壞情況樹退化成鏈狀時是 O(n))

# Pattern 筆記:
# 這題的 pattern 是「DFS 遞迴修改樹結構」,
# 下次看到「需要對整棵樹的每個節點做結構性修改(而不是只收集數值)」的特徵就用這個方法。