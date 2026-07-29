# 895 - Maximum Frequency Stack
# https://leetcode.com/problems/maximum-frequency-stack/
# Hard | Stack
# 思路: 用兩個 dictionary 搭配一個 maxFreq 變數:
# freq 記錄每個數值目前出現過幾次。
# freqStack(用 defaultdict(list))的 key 是頻率數字,value 是一個 stack(list),
# 存的是「曾經在這個頻率達到時,被 push 進來的數值」,依照 push 順序疊放。
# 同一個數值會同時存在於好幾個不同頻率的分組裡,不需要「搬移」,
# 每次頻率增加時,單純往新的頻率分組 append 即可。
# push(val) 的時候:
# 更新 freq[val](第一次出現設成 1,之後累加 1),
# 把 val 加進 freqStack[freq[val]] 這組 stack,
# 如果這個新頻率比目前的 maxFreq 還大,更新 maxFreq。
# pop() 的時候:
# 直接從 freqStack[maxFreq] 這組 pop 出 top(因為這組代表目前最高頻率、
# 且 stack 的 LIFO 特性確保拿到的是「最近被 push 到這個頻率」的數值),
# 把這個數值的 freq 減 1,
# 如果 freqStack[maxFreq] 被 pop 空了,代表這個最高頻率已經沒有元素了,
# maxFreq 要減 1,回到次高頻率。
# Pattern 筆記: 這題的 pattern 是用「按某個統計值(頻率)分組的多個 stack」
# 搭配一個追蹤目前最大值的變數,下次看到「需要 O(1) 找到符合某個最值條件、
# 且同條件下要按 LIFO 順序處理」這種特徵就用這個方法。
# Time: push / pop 均為 O(1) | Space: O(n)

class FreqStack:

    def __init__(self):
        self.freq = {}
        self.freqStack = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        if not val in self.freq:
            self.freq[val] = 1
        else:
            self.freq[val] += 1
        self.freqStack[self.freq[val]].append(val)
        if self.freq[val] > self.maxFreq:
            self.maxFreq = self.freq[val]

    def pop(self) -> int:
        res = self.freqStack[self.maxFreq].pop()
        self.freq[res] -= 1
        if self.freqStack[self.maxFreq] == []:
            self.maxFreq -= 1
        return res