# 344. Reverse String
# https://leetcode.com/problems/reverse-string/
# 難度：Easy
# 類型：Two Pointers

# 思路：
# 用左右兩個指標，分別指向陣列的第一個和最後一個位置。
# 只要 left < right，就交換兩個指標所在的元素，
# 交換完之後 left 往右移一格、right 往左移一格，持續往中間收斂。
# 當 left == right 或 left > right 時代表已經處理完所有需要交換的位置，迴圈結束。
# 如果陣列長度是奇數，中間那個元素因為前後對稱不會被交換到，但也不需要被交換，
# 因為它本來的位置就是正確的。

# Pattern 筆記：
# 這題的 pattern 是「左右指標對撞（opposite direction two pointers）」，
# 下次看到「需要原地反轉陣列/字串」或「頭尾對稱比較」的特徵就用這個方法。

# Time: O(n)
# Space: O(1)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            # 交換 left 跟 right 位置上的字元
            s[left], s[right] = s[right], s[left]
            # 兩個指標分別往中間移動一格
            left += 1
            right -= 1