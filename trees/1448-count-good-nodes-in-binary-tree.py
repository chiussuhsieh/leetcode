# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Difficulty: Medium
# Type: Tree / DFS Recursion (Top-down 傳遞路徑資訊)

# 思路:
# 用 DFS 走訪整棵樹,遞迴時把「從根到目前節點之前,路徑上的最大值」一路往下傳
# 1. 定義輔助函式 dfs(node, maxSoFar),maxSoFar 是路徑上目前看過的最大值
# 2. base case:如果 node 是 None,好節點數量是 0
# 3. 如果 node.val >= maxSoFar,代表路徑上沒有比它大的節點,它是好節點,count 設為 1,
#    並把 maxSoFar 更新成 node.val
# 4. 遞迴呼叫左子樹和右子樹(傳入更新後的 maxSoFar),把回傳的好節點數量加進 count
# 5. 回傳 count
# 6. 初始呼叫 dfs(root, root.val),用根的值當初始最大值,所以根一定是好節點(也不受負數影響)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSoFar):
            if not node:
                return 0
            count = 0
            if node.val >= maxSoFar:
                maxSoFar = node.val
                count = 1
            count += dfs(node.left, maxSoFar)
            count += dfs(node.right, maxSoFar)
            return count
        return dfs(root, root.val)

# Time Complexity: O(n) 每個節點只被訪問一次
# Space Complexity: O(h) 遞迴呼叫堆疊的深度,h 是樹高,最壞情況(鏈狀)是 O(n)

# Pattern 筆記:
# 這題的 pattern 是「DFS 遞迴時,把路徑上累積的資訊(例如最大值)當參數往下傳」,
# 下次看到「節點的判斷取決於從根走到它的路徑」的特徵就用這個方法。