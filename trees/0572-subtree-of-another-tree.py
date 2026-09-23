# https://leetcode.com/problems/subtree-of-another-tree/
# Difficulty: Easy
# Type: Tree / DFS Recursion (Dual-tree comparison + search for starting point)

# 思路:
# 建立在 isSameTree 之上,對 root 的每個節點分別當作起點,檢查是否跟 subRoot 完全相同
# 1. base case:如果 root 是 None(還沒找到匹配就走到底),回傳 False
# 2. 如果 subRoot 是 None(空樹永遠是任何樹的子樹),回傳 True
# 3. 先用 isSameTree 檢查「以目前 root 為起點」是否跟整個 subRoot 完全相同,是的話回傳 True
# 4. 否則換新的起點繼續找:對 root.left 或 root.right 分別遞迴呼叫 isSubtree(subRoot 保持不變),
#    只要其中一邊找到就回傳 True(用 or 連接)
# isSameTree 部分:
# 5. 兩邊都是 None,結構相同,回傳 True
# 6. 只有一邊是 None,結構不同,回傳 False
# 7. 節點值不同,回傳 False
# 8. 否則遞迴比較左右子樹是否都相同

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        else:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

# Time Complexity: O(m * n) — m 是 root 的節點數,n 是 subRoot 的節點數
#                  最壞情況下,對 root 的每個節點都要做一次 O(n) 的 isSameTree 比對
# Space Complexity: O(m + n) — 遞迴呼叫堆疊(isSubtree 的深度 + isSameTree 的深度)

# Pattern 筆記:
# 這題的 pattern 是「在既有的雙樹比較函式基礎上,外層再包一層遞迴,對每個節點都嘗試當作起點」,
# 下次看到「需要在一棵樹中找出某個結構是否作為子結構出現」的特徵就用這個方法。