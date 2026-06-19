# 269. Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/
# 難度：Hard
# 類型：Graph (Topological Sort, BFS / Kahn's Algorithm)

# 思路：
# 比較相鄰的單字，找第一個不同的字母，可以推斷出「誰要排在誰前面」
# 用這些先後關係建立一個圖，然後做 Topological Sort 排出合法順序
# 用 Kahn's Algorithm（BFS 版本）：
# 1. 算出每個字母的 in-degree（有幾個字母規定要排在它前面）
# 2. 從 in-degree=0 的字母開始（沒有限制，可以最先排）
# 3. 排好一個字母後，把它指向的字母 in-degree -1
# 4. in-degree 變 0 就加入隊列繼續處理
# 如果排完的數量 < 所有字母數量，代表有環（互相矛盾），無解

# Time: O(C)，C 是所有單字的總字元數
# Space: O(1)，最多 26 個字母

from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)             # key=字母, value=這個字母指向的字母集合
        in_degree = {c: 0 for word in words for c in word}
        # 先把所有出現過的字母都初始化 in_degree = 0

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]    # 比較相鄰兩個單字
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
                # 邊界情況：例如 ["abc","ab"]，較長的字串卻排在前面，順序不合法

            for j in range(min_len):
                if w1[j] != w2[j]:
                    # 找到第一個不同的字母，代表 w1[j] 應該排在 w2[j] 前面
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])      # 建立邊：w1[j] → w2[j]
                        in_degree[w2[j]] += 1         # w2[j] 多一個「要排在它前面」的字母
                    break
                    # 只看第一個不同的字母，後面的字母順序這裡判斷不出來，不用再比

        queue = deque([c for c in in_degree if in_degree[c] == 0])
        # 把所有沒有限制（in_degree=0）的字母放入隊列，可以最先排

        result = []

        while queue:
            c = queue.popleft()
            result.append(c)                 # 排進結果

            for neighbor in graph[c]:
                in_degree[neighbor] -= 1
                # c 已經排好了，它指向的字母少一個限制

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    # 這個字母的限制都解除了，可以排了，加入隊列

        if len(result) != len(in_degree):
            return ""
            # 排出來的數量比實際字母少，代表有環（互相矛盾），無法排序

        return "".join(result)   # 合法的字母順序