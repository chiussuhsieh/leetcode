# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Difficulty: Medium
# Type: Tree / BST Property (Binary Search style pruning)

# 思路:
# 利用 BST「左小右大」的性質,沿著一條路徑往下找分岔點,不需要遍歷整棵樹
# 1. 如果 p 和 q 的值都小於 root.val,代表兩者都在左子樹,往左遞迴繼續找
# 2. 如果 p 和 q 的值都大於 root.val,代表兩者都在右子樹,往右遞迴繼續找
# 3. 其他情況(一個在左一個在右,或其中一個等於 root.val),代表 root 就是分岔點,
#    也就是最低共同祖先,直接回傳 root
# 因為題目保證 p、q 一定存在於樹中,遞迴必定會在某一步命中情況 3,不需要額外處理 root 是 None 的 base case

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

# Time Complexity: O(h) — h 是樹的高度,每一步都只往一個方向走,不需要遍歷整棵樹
#                  最壞情況(樹退化成鏈狀)是 O(n),平衡樹則是 O(log n)
# Space Complexity: O(h) — 遞迴呼叫堆疊的深度

# Pattern 筆記:
# 這題的 pattern 是「利用 BST 左小右大的性質做剪枝,沿單一路徑往下走而非遍歷整棵樹」,
# 下次看到「BST + 需要判斷節點相對位置(找路徑、找祖先)」的特徵就用這個方法。