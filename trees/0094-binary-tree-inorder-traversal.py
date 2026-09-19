# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Difficulty: Easy
# Type: Tree / DFS Traversal

# 思路:
# 用遞迴做 inorder traversal(左 -> 根 -> 右)
# 1. base case:如果 root 是 None,回傳空 list
# 2. 先遞迴呼叫自己拿到左子樹的 inorder 結果
# 3. 再遞迴呼叫自己拿到右子樹的 inorder 結果
# 4. 用 for loop 把左子樹的結果加進 res,接著放入根節點的值,最後用 for loop 把右子樹的結果加進 res
# 5. 回傳 res

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        if not root:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        for val in left:
            res.append(val)
        res.append(root.val)
        for val in right:
            res.append(val)
        return res

# Time Complexity: O(n) — 每個節點恰好被訪問一次
# Space Complexity: O(n) — 遞迴呼叫堆疊,加上儲存結果的 res

# Pattern 筆記:
# 這題的 pattern 是「DFS 遞迴走訪,只是根節點放入 res 的時機點在左右子樹之間」,
# 下次看到「需要依照特定順序(尤其是排序性質)收集節點值」的特徵就用這個方法。