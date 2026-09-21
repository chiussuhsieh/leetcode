# https://leetcode.com/problems/same-tree/
# Difficulty: Easy
# Type: Tree / DFS Recursion (Dual-tree comparison)

# 思路:
# 同時遞迴走訪兩棵樹 p 和 q,逐一比較對應節點
# 1. 如果 p 和 q 都是 None,結構相同,回傳 True
# 2. 如果只有一個是 None(另一個不是),結構不同,回傳 False
# 3. 如果兩個節點值不同,回傳 False
# 4. 否則遞迴比較左子樹和右子樹是否都相同(用 and 連接,兩邊都要為 True)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Time Complexity: O(n) — 最壞情況要走訪兩棵樹所有節點(n 是較小那棵樹的節點數)
# Space Complexity: O(n) — 遞迴呼叫堆疊(最壞情況樹退化成鏈狀時是 O(n))

# Pattern 筆記:
# 這題的 pattern 是「雙樹同步 DFS 遞迴比較」,
# 下次看到「需要同時走訪兩棵樹、逐節點比對」的特徵就用這個方法。