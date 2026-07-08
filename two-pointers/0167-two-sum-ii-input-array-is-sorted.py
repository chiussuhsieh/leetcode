# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# 難度：Medium
# 類型：Two Pointers

# 思路：
# 陣列已經排序好，用 left 指向最左邊、right 指向最右邊，從兩個極端值往中間逼近 target。
# 如果 numbers[left] + numbers[right] > target：總和太大，把 right 往左移一格，
# 因為 numbers[left] 配上 right 或 right 右邊任何數字，總和只會更大、不可能是答案，
# 只有 right 左邊的數字還有機會，所以安全地把 right 往左移，left 保持不動。
# 如果總和 < target：邏輯相反，把 left 往右移一格，讓總和變大。
# 如果剛好等於 target：找到答案，回傳兩個索引 + 1（題目要求索引從 1 開始）。

# Pattern 筆記：
# 這題的 pattern 是「排序陣列上的雙指標收斂（converging two pointers on sorted array）」，
# 下次看到「已排序陣列」且「找兩數之和等於特定 target」的特徵就用這個方法。

# Time: O(n)
# Space: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                # 總和太大，右指標左移讓總和變小
                right -= 1
            else:
                # 總和太小，左指標右移讓總和變大
                left += 1