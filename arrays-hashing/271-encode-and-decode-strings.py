# 271. Encode and Decode Strings
# https://neetcode.io/problems/string-encode-and-decode
# 難度：Medium
# 類型：Array, String
# 思路：
# encode：每個字串前面加上「長度#」，例如 ["hello", "world"] → "5#hello5#world"
# decode：用兩個指針 i 和 j
# i 永遠指向這一段「長度數字」的第一個字元（每輪結束後跳到下一段起點）
# j 從 i 出發往右找到 # 的位置，s[i:j] 就是完整的長度數字
# 再從 # 後面切出對應長度的字串
# 即使內容裡有 #，也不影響解析，因為靠長度切字串而不是靠 # 分隔
# Pattern 筆記：
# 這題的 pattern 是「長度前綴編碼（Length-Prefix Encoding）」
# encode 用「長度#內容」格式，decode 用指針找 # 讀長度再切字串
# 下次看到「需要把 array of strings 編碼成單一字串且內容可能含特殊字符」就用這個方法
# Time: O(n)
# Space: O(n)

from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s  # 長度 + # + 內容
        return ans

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i                          # j 從這段數字的第一個字元出發
            while s[j] != "#":            # j 往右找 # 的位置
                j += 1
            length = int(s[i:j])          # s[i:j] 是完整的長度數字
            word = s[j+1: j+1+length]     # # 後面切出對應長度的字串
            res.append(word)
            i = j+1+length                # 跳到下一段數字的第一個字元
        return res