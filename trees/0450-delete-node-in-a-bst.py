# https://leetcode.com/problems/delete-node-in-a-bst/
# Difficulty: Medium
# Type: Tree / BST Property (Recursion + helper function)

# 思路:
# 分兩階段處理:先利用 BST 性質找到要刪除的節點,再依照該節點的子節點數量分四種情況處理
# 1. base case:如果 root 是 None,代表 key 不存在,回傳 None
# 2. 如果 key < root.val,遞迴刪除左子樹中的節點,回傳值重新接回 root.left
# 3. 如果 key > root.val,遞迴刪除右子樹中的節點,回傳值重新接回 root.right
# 4. 如果 key == root.val,找到要刪除的節點,分四種情況處理:
#    a. 葉節點(左右都沒有):直接變成 None
#    b. 只有左子節點:左子樹直接頂上
#    c. 只有右子節點:右子樹直接頂上
#    d. 左右都有子節點:用 findMin 找出右子樹中最小的節點,把它的值複製到 root.val,
#       再遞迴刪除右子樹中原本那個最小節點(因為值已經被複製走,不能重複存在)
# 5. 回傳 root,讓上一層能接住結果並重新接上
# findMin 輔助函式:
# 6. 從 node 開始不斷往左走,直到沒有左子節點為止,回傳該節點(即最小值節點)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        if key == root.val:
            if not root.left and not root.right:
                root = None
            elif root.left and not root.right:
                root = root.left
            elif not root.left and root.right:
                root = root.right
            elif root.left and root.right:
                minRight = self.findMin(root.right)
                root.val = minRight.val
                root.right = self.deleteNode(root.right, minRight.val)
        return root

    def findMin(self, node):
        cur = node
        while cur.left:
            cur = cur.left
        return cur

# Time Complexity: O(h) — h 是樹的高度,找節點跟找最小值都只沿著一條路徑走
#                  最壞情況(樹退化成鏈狀)是 O(n),平衡樹則是 O(log n)
# Space Complexity: O(h) — 遞迴呼叫堆疊的深度

# Pattern 筆記:
# 這題的 pattern 是「BST 刪除,依節點的子節點數量分情況處理,雙子節點時用『找繼承者(右子樹最小值)+ 複製值 + 遞迴刪除繼承者』的技巧」,
# 下次看到「BST 結構修改且節點可能同時有左右子樹」的特徵就用這個方法。