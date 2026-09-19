# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Difficulty: Easy
# Type: Tree / DFS Traversal

# 思路:
# 用遞迴做 postorder traversal(左 -> 右 -> 根)
# 1. base case:如果 root 是 None,回傳空 list(維持回傳型別一致,才能被 for loop 遍歷)
# 2. 先遞迴呼叫自己拿到左子樹的 postorder 結果,用 for loop 加進 res
# 3. 再遞迴呼叫自己拿到右子樹的 postorder 結果,用 for loop 加進 res
# 4. 最後才把根節點的值放進 res
# 5. 回傳 res

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        if not root:
            return []
        left = self.postorderTraversal(root.left)
        for val in left:
            res.append(val)
        right = self.postorderTraversal(root.right)
        for val in right:
            res.append(val)
        res.append(root.val)
        return res

# Time Complexity: O(n) — 每個節點恰好被訪問一次
# Space Complexity: O(n) — 遞迴呼叫堆疊,加上儲存結果的 res

# Pattern 筆記:
# 這題的 pattern 是「DFS 遞迴走訪,根節點放入 res 的時機點在左右子樹都處理完之後」,
# 下次看到「需要先處理完所有子節點才能處理自己」的特徵就用這個方法(例如樹上 DP)。