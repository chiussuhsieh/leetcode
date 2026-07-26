# 150 - Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Medium | Stack
# 思路: 用 stack 存數字,單次掃描 tokens。
# 如果目前 token 是運算符號("+"、"-"、"*"、"/"),
# 就從 stack pop 出最近的兩個數字:
# 因為 stack 是 LIFO,第一次 pop 出來的數字要放在運算符號右邊,
# 第二次 pop 出來的數字要放在運算符號左邊(減法、除法的順序不能顛倒)。
# 算完之後把結果 push 回 stack,讓它可以被之後的運算符號使用。
# 如果目前 token 不是運算符號(是數字字串),就轉成 int 後 push 進 stack。
# 除法用 int(b/a) 而不是 b//a,因為 int() 對浮點數是無條件捨去到 0 的方向(truncate toward zero),
# 而 // 是無條件捨去到負無窮,遇到負數結果會不同,題目要求要用前者。
# 最後 stack 裡只會剩下一個元素,就是最終答案。
# Pattern 筆記: 這題的 pattern 是用 stack 處理運算式求值,單次掃描、
# 遇到運算元就 push、遇到運算符號就 pop 出最近的運算元來運算,
# 下次看到「後綴/逆波蘭表示法」或「運算需要依賴最近算出的中間結果」這種特徵就用這個方法。
# Time: O(n) | Space: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]