# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Difficulty: Medium
# Type: Tree / BST Property (Recursion with reassignment)

# 思路:
# 利用 BST 左小右大的性質,沿著路徑往下找到正確的空位插入新節點
# 1. base case:如果 root 是 None,代表找到空位,建立新節點 TreeNode(val) 並指派給 root
# 2. 如果 val 小於 root.val,遞迴呼叫插入到左子樹,並把回傳值重新指派回 root.left(確保新節點被接上樹)
# 3. 如果 val 大於 root.val,同理處理右子樹
# 4. 回傳 root,讓上一層能接住這一層的結果並重新接上

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root == None:
            newNode = TreeNode(val)
            root = newNode
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root

# Time Complexity: O(h) — h 是樹的高度,沿著一條路徑往下走
#                  最壞情況(樹退化成鏈狀)是 O(n),平衡樹則是 O(log n)
# Space Complexity: O(h) — 遞迴呼叫堆疊的深度

# Pattern 筆記:
# 這題的 pattern 是「BST 插入,遞迴時用『回傳並重新接上』的模式(root.left = self.func(root.left, ...))」,
# 下次看到「需要修改樹的結構,並確保修改後的子樹被正確接回父節點」的特徵就用這個方法。