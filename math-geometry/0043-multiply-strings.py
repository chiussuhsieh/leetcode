# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/
# 難度：Medium
# 類型：Math, String

# 思路：
# 模擬小學直式乘法，一位一位相乘再加總
# num1[i] 和 num2[j] 相乘，結果放在 result[i+j] 和 result[i+j+1] 的位置
# result 陣列長度最多是 len(num1) + len(num2)
# 從右到左掃兩個字串，每次相乘後處理進位
# 最後把 result 陣列轉成字串，去掉前導零

# Time: O(m*n)，m 和 n 是兩個字串的長度
# Space: O(m+n)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"   # 任何數乘以 0 都是 0，直接回傳

        result = [0] * (len(num1) + len(num2))
        # 結果最多 m+n 位數，先建立一個全 0 的陣列

        for i in range(len(num1) - 1, -1, -1):      # 從右到左掃 num1
            for j in range(len(num2) - 1, -1, -1):  # 從右到左掃 num2
                mul = int(num1[i]) * int(num2[j])    # 兩個位數相乘
                p1, p2 = i + j, i + j + 1            # 結果放在 p1（十位）和 p2（個位）
                total = mul + result[p2]              # 加上之前存在 p2 的值（可能有進位）
                result[p2] = total % 10               # 個位數放 p2
                result[p1] += total // 10             # 進位加到 p1

        result_str = ""
        for d in result:
            result_str += str(d)   # 把每個數字轉成字串串接起來

        result_str = result_str.lstrip("0")
        # 去掉前導零，例如 "00123" → "123"

        return result_str if result_str else "0"
        # 如果 result_str 是空字串（全部都是0），回傳 "0"