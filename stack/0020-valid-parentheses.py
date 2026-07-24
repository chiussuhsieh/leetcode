# 20 - Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Easy | Stack
# 思路: 建立一個 hashmap,key 是右括號、value 是對應的左括號。
# 逐一掃描字串,如果字元是右括號(存在於 hashmap 的 key 裡),
# 就檢查 stack 是否為空、且 stack 最上面的元素是否等於該右括號對應的左括號,
# 符合的話就把 stack 最上面的元素 pop 掉;不符合就直接 return False。
# 如果字元不是右括號(也就是左括號),就把它 push 進 stack。
# 掃完整個字串後,檢查 stack 是否為空:
# 如果是空的代表所有括號都配對完成,回傳 True;
# 如果還有剩,代表有左括號沒被配對到,回傳 False。
# Pattern 筆記: 這題的 pattern 是用 stack 處理巢狀配對結構,下次看到「括號配對」、
# 「巢狀結構最內層要先被處理/關閉」這種特徵就用這個方法。
# Time: O(n) | Space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False