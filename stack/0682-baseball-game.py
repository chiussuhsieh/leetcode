# 682 - Baseball Game
# https://leetcode.com/problems/baseball-game/
# Easy | Stack
# 思路: 建立一個 rounds array(當作 stack)存每一輪的有效分數。
# 逐一掃描 operations 陣列:
# 如果是 "+",取 stack 最上面兩個分數相加,把結果 push 進去。
# 如果是 "D",取 stack 最上面的分數乘以二,把結果 push 進去。
# 如果是 "C",把 stack 最上面的分數 pop 掉(取消上一輪)。
# 如果都不是上述三種情況,代表是代表分數的數字字串(可能是負數),
# 轉成 int 之後 push 進 stack。
# 最後回傳 stack 裡所有分數的總和(因為被取消的分數已經被 pop 掉了)。
# Pattern 筆記: 這題的 pattern 是用 stack 動態根據輸入做 push/pop,
# 下次看到「每一步操作都依賴前面已經算出的結果」這種特徵就用這個方法。
# Time: O(n) | Space: O(n)

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rounds = []

        for element in operations:
            if element == "+":
                point = rounds[-1] + rounds[-2]
                rounds.append(point)
            elif element == "D":
                newPoint = rounds[-1] * 2
                rounds.append(newPoint)
            elif element == "C":
                rounds.pop()
            else:
                rounds.append(int(element))

        return sum(rounds)