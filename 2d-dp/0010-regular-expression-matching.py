# 10. Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/
# 難度：Hard
# 類型：2D DP

# 思路：
# dp[i][j] = s 前 i 個字元和 p 前 j 個字元能不能匹配
# 對每個 (i, j)，看 p[j-1] 是什麼來決定怎麼轉移：
# 1. p[j-1] 是普通字元或 '.'：
#    s[i-1] 跟 p[j-1] 匹配（相同，或 p[j-1]='.'）且 dp[i-1][j-1] 成立 → True
# 2. p[j-1] 是 '*'：兩種選擇
#    a. 把 "前一個字元*" 當作出現 0 次：直接看 dp[i][j-2]
#    b. 如果 s[i-1] 跟 p[j-2] 匹配，可以讓 "*" 多吃一個字元：看 dp[i-1][j]
# base case：dp[0][0]=True（空字串對空 pattern）
#            dp[0][j]：只有形如 "a*b*c*" 這種純 "*" 結構才能匹配空字串
# 注意：不能在字元不匹配時直接 return False，因為後面的 '*' 可能讓結果改變，
#       必須把所有 (i,j) 組合都算過


# Time: O(m*n)
# Space: O(m*n)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = []
        for i in range(m + 1):
            row = []
            for j in range(n + 1):
                row.append(False)
            dp.append(row)

        dp[0][0] = True   # 空字串對空 pattern，匹配成功

        # base case：s 是空字串，只有 "x*y*z*" 這種結構的 pattern 能匹配
        for j in range(1, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
                # "*" 讓前一個字元出現 0 次，相當於忽略前兩個字元

        for i in range(1, m + 1):           # i 對應 s 的 index
            for j in range(1, n + 1):       # j 對應 p 的 index
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    # 注意：跟 s 比對一律用 s[i-1]，不能寫成 s[j-1]
                    dp[i][j] = dp[i-1][j-1]
                    # 字元匹配（或是 '.' 萬用字元），繼承左上角結果

                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    # 選擇A：這個 "字元*" 出現 0 次，忽略它

                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                        # 選擇B：如果前一個字元能匹配 s[i-1]，"*" 可以多吃一個字元

        return dp[m][n]