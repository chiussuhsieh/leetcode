# 0003. Longest Substring Without Repeating Characters (Mock Interview 練習)
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 難度：Medium
# 類型：Sliding Window
# 備註：此題為與同學進行 mock interview 的練習紀錄，非首次正式解題（正式解題紀錄在 sliding-window/ 資料夾）

"""
Given a string s, find the length of the longest substring
without repeating characters.

Example 1:
  Input:  s = "abcadefg"
  Output: 3
  Explanation: The answer is "abc", with length 3.

Example 2:
  Input:  s = "bbbbb"
  Output: 1
  Explanation: The answer is "b", with length 1.

Example 3:
  Input:  s = "pwwkew"
  Output: 3
  Explanation: The answer is "wke", with length 3.
  Note: "pwke" is a subsequence, not a substring.

Constraints:
  0 <= s.length <= 5 * 10^4
  s consists of English letters, digits, symbols.
"""

# 思路：
# 用 sliding window 搭配 set 紀錄目前視窗內出現過的字元。
# left、right 兩個指標框住視窗範圍，right 負責往右擴張視窗，逐一檢查新字元。
# 如果 s[right] 還沒出現在 set 裡，代表視窗可以繼續擴張：加入 set，curLength 加一，
# 並更新 maxLength。
# 如果 s[right] 已經出現在 set 裡（代表重複了），就用 while 迴圈持續從 set 移除
# s[left]、left 右移、curLength 減一，直到 s[right] 這個重複的字元被移出視窗為止，
# 再把 s[right] 加入 set。
# 走訪完整個字串後，maxLength 就是答案。

# Pattern 筆記：
# 這題的 pattern 是 sliding window + set 判斷重複，下次看到「找最長的不重複子字串／子陣列」
# 的特徵就用這個方法：右指標負責擴張視窗，遇到重複就用內層 while 讓左指標持續收縮，
# 直到視窗內不再重複為止。

# Time complexity: O(n)，每個字元最多被 left、right 各訪問一次
# Space complexity: O(min(n, m))，m 為字元集大小，取決於 set 最多能存多少不重複字元

def longestSubstring(s):
    curLength = 0  # 目前視窗內不重複字元的長度
    maxLength = 0  # 目前為止見過最長的不重複長度
    left, right = 0, 0  # 視窗的左右指標
    sSet = set()  # 記錄目前視窗內出現過的字元
    for right in range(len(s)):  # right 負責擴張視窗
        if s[right] not in sSet:  # 沒有重複，可以直接擴張
            sSet.add(s[right])
            curLength += 1
            maxLength = max(curLength, maxLength)
        else:  # 遇到重複字元，持續收縮左邊界直到重複消失
            while s[right] in sSet:
                sSet.remove(s[left])
                left += 1
                curLength -= 1
            sSet.add(s[right])
    return maxLength


test_cases = [
    ("abcabcbb",  3),    # "abc"
    ("bbbbb",     1),    # "b"
    ("pwwkew",    3),    # "wke"
    ("",          0),
    ("a",         1),
    ("abcdef",    6),
    ("abba",      2),    # "ab" 然後 "ab"，關鍵陷阱
    ("aab",       2),    # "ab"
    ("dvdf",      3),    # "vdf"
    ("1231234",   4),    # "1234"... 實際是 "2312" 之類，長度 4
    ("abababab",  2),    # "ab"
    ("tmmzuxt",   5),    # "mzuxt"
]

for i, (s, expected) in enumerate(test_cases):
    result = longestSubstring(s)
    status = "PASS" if result == expected else "FAIL"
    print(f"Test {i+1}: {status}  input={s!r}  got={result}  expected={expected}")
    assert result == expected, f"Test {i+1} failed"

print("\nAll tests passed!")