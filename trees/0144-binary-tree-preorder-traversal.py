# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Difficulty: Easy
# Type: Tree / DFS Traversal

# 思路:
# 用遞迴做 preorder traversal(根 -> 左 -> 右)
# 1. base case:如果 root 是 None,回傳空 list
# 2. 先把根節點的值放進 res
# 3. 遞迴呼叫自己拿到左子樹的 preorder 結果(是一個 list),用 for loop 把裡面每個值逐一加進 res
# 4. 再遞迴呼叫自己拿到右子樹的 preorder 結果,一樣用 for loop 加進 res
# 5. 回傳 res

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        if not root:
            return []
        res.append(root.val)
        left = self.preorderTraversal(root.left)
        for val in left:
            res.append(val)
        right = self.preorderTraversal(root.right)
        for val in right:
            res.append(val)
        return res

# Time Complexity: O(n) — 每個節點恰好被訪問一次
# Space Complexity: O(n) — 遞迴呼叫堆疊(最壞情況樹退化成鏈狀時是 O(n)),加上儲存結果的 res 也是 O(n)

# Pattern 筆記:
# 這題的 pattern 是「DFS 遞迴走訪 + 用遞迴回傳值組合結果」,
# 下次看到「走訪整棵樹並依照特定順序收集節點值」的特徵就用這個方法。