# 71 - Simplify Path
# https://leetcode.com/problems/simplify-path/
# Medium | Stack
# 思路: 先用 path.split("/") 把路徑字串依照 "/" 拆成一段一段。
# 用 stack 存目前有效的資料夾名稱,逐一掃描拆分後的每一段 p:
# 如果 p 是空字串(通常是開頭、結尾,或連續 "//" 造成的),直接忽略。
# 如果 p 是 "."(代表當前目錄,原地不動),直接忽略。
# 如果 p 是 ".."(代表要回到上一層目錄):
#   如果 stack 不是空的,把 stack 最上面的資料夾 pop 掉(回到上一層);
#   如果 stack 是空的(已經在根目錄,沒有上一層可以回去),什麼都不做。
# 如果都不是以上情況,代表 p 是一般的資料夾名稱,push 進 stack。
# 最後把 stack 裡的內容用 "/" 串接起來,前面再加上一個 "/" 開頭,
# 組成最終的絕對路徑字串(如果 stack 是空的,結果就會是根目錄 "/")。
# Pattern 筆記: 這題的 pattern 是用 stack 處理路徑字串解析,
# 下次看到「需要根據不同 token 動態決定 push/pop/忽略」、
# 「.. 代表回上一層」這種特徵就用這個方法。
# Time: O(n) | Space: O(n)

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for p in path:
            if p == "":
                continue
            elif p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(p)
        res = "/" + "/".join(stack)
        return res