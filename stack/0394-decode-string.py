# 394 - Decode String
# https://leetcode.com/problems/decode-string/
# Medium | Stack
# 思路: 用 curNum 記錄目前正在收集的數字(倍數),用 curS 記錄目前正在收集的字串。
# 用 stack 存 (curNum, curS) 的 tuple,代表進入下一層之前,上一層已經收集好的狀態。
# 單次掃描字串 s:
# 如果是數字字元,用 curNum = curNum * 10 + int(element) 累加,
# 這樣可以正確組合多位數(例如 "12")。
# 如果是英文字母,直接用 curS += element 累加到目前字串。
# 如果是 "["(進入新的一層):
#   把目前的 (curNum, curS) push 進 stack 保存起來,
#   然後把 curNum 重設為 0、curS 重設為空字串,準備收集這一層裡面的內容。
# 如果是 "]"(這一層結束了):
#   從 stack pop 出 (oldNum, oldS),也就是進入這一層之前的倍數和已收集字串。
#   計算這一層展開後的結果:curS = oldS + oldNum * curS,
#   代表「上一層已收集的字串」加上「這一層的倍數 × 這一層收集到的字串」,
#   並把這個結果存回 curS,讓它可以繼續被外層使用(由內而外逐層展開)。
# 掃完整個字串後,curS 就是最終展開完成的答案。
# Pattern 筆記: 這題的 pattern 是用 stack 處理需要暫存多層狀態的巢狀字串解析,
# 下次看到「巢狀括號結構,且每一層都需要各自累積狀態(數字、字串等)」這種特徵就用這個方法。
# Time: O(n * k),k 是展開後字串的長度 | Space: O(n)

class Solution:
    def decodeString(self, s: str) -> str:
        curNum = 0
        curS = ""
        stack = []
        for element in s:
            if element.isdigit():
                curNum = curNum * 10 + int(element)
            elif element.isalpha():
                curS += element
            elif element == "[":
                stack.append((curNum, curS))
                curNum = 0
                curS = ""
            elif element == "]":
                oldNum, oldS = stack.pop()
                curS = oldS + oldNum * curS
        return curS