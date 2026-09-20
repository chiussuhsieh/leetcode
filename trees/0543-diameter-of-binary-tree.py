# https://leetcode.com/problems/diameter-of-binary-tree/
# Difficulty: Easy
# Type: Tree / DFS Recursion (Bottom-up + Global Tracking)

# 思路:
# 用一個內部函式 diameter 計算每個節點的高度,同時用 self.res 追蹤全域最大直徑
# 1. base case:如果 root 是 None,直接回傳 0
# 2. 用巢狀函式 diameter(cur) 計算高度,並在過程中順便更新全域最大值
# 3. base case(cur 是 None):高度為 0
# 4. 遞迴呼叫拿到 left 和 right,分別是左右子樹的高度
# 5. 「經過 cur 這個節點」的路徑長度是 left + right,用這個值更新 self.res(因為答案不一定經過 root)
# 6. 回傳 cur 自己的高度給上一層:1 + max(left, right)
# 7. 呼叫 diameter(root) 觸發整個遞迴,最後回傳 self.res

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 0
        def diameter(cur):
            if not cur:
                return 0
            left = diameter(cur.left)
            right = diameter(cur.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        diameter(root)
        return self.res

# Time Complexity: O(n) — 每個節點只被訪問一次
# Space Complexity: O(n) — 遞迴呼叫堆疊(最壞情況樹退化成鏈狀時是 O(n))

# Pattern 筆記:
# 這題的 pattern 是「DFS 遞迴回傳單一數值(高度)給上一層使用,但同時用 self.xxx 或 nonlocal 追蹤一個全域最大值」,
# 下次看到「答案不一定發生在根節點,而可能是樹中任意節點」的特徵就用這個方法。