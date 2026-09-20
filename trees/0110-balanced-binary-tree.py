# https://leetcode.com/problems/balanced-binary-tree/
# Difficulty: Easy
# Type: Tree / DFS Recursion (Bottom-up)

# 思路:
# 用一個內部函式 depth,同時計算「深度」和「是否平衡」,避免對每個節點重複呼叫 maxDepth 造成 O(n^2)
# 1. base case:如果 root 是 None,深度是 0,視為平衡,回傳 [0, True]
# 2. 遞迴呼叫 depth(root.left) 和 depth(root.right),分別拿到 [左深度, 左是否平衡] 和 [右深度, 右是否平衡]
# 3. 以 root 為根的深度 = 左右子樹深度較大值 + 1(不管平不平衡都要算)
# 4. 以 root 為根是否平衡,需同時滿足三個條件:左子樹平衡、右子樹平衡、且左右深度差不超過 1
# 5. 把 [深度, 是否平衡] 包成 list 回傳
# 6. isBalanced 主體呼叫 depth(root),取回傳結果的第二個值(是否平衡)當最終答案

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root):
            if not root:
                return [0, True]
            left = depth(root.left)
            right = depth(root.right)
            if left[1] and right[1] and abs(left[0] - right[0]) <= 1:
                return [1 + max(left[0], right[0]), True]
            else:
                return [1 + max(left[0], right[0]), False]
        res = depth(root)
        return res[1]

# Time Complexity: O(n) — 每個節點只被訪問一次,深度跟平衡判斷在同一次遞迴中完成
# Space Complexity: O(n) — 遞迴呼叫堆疊(最壞情況樹退化成鏈狀時是 O(n))

# Pattern 筆記:
# 這題的 pattern 是「DFS 遞迴時,用一次走訪同時回傳多個資訊(打包成 list/tuple),避免對同一棵子樹重複計算」,
# 下次看到「需要子樹的多種資訊(例如深度 + 某個判斷條件)才能組合出當前節點答案」的特徵就用這個方法。