# 332. Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/
# 難度：Hard
# 類型：Graph (Eulerian Path, DFS)

# 思路：
# 這題要求「用完所有邊」（每張機票必須用一次），這是 Eulerian Path 問題
# 不是找最短路徑，而是找一條「走完所有邊」的路徑，且字典順序最小
# 核心想法：用 DFS，每次都優先選字典順序最小的下一站
# 但這樣貪心可能會走到死路（卡住，還有票沒用完）
# 解法：用「先深入再記錄」的技巧（Hierholzer's Algorithm）
#   先一路 DFS 走到底（走到沒有票可用為止），把走過的點記下來
#   走到死路後，回溯時才把這個點加入結果（用 append，最後 reverse）
#   這樣可以保證：死路會被排到結果的最後面，不會卡住整條路徑

# Time: O(E log E)，E 是邊數，排序機票
# Space: O(E)

from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)
            # 用 min heap 存每個機場可以飛到哪裡，heap 保證字典順序最小的會先被彈出

        route = []

        def dfs(airport):
            while graph[airport]:
                next_dest = heapq.heappop(graph[airport])
                # 優先選字典順序最小的下一站

                dfs(next_dest)
                # 先深入走下去

            route.append(airport)
            # 這個機場已經沒有票可以飛了（死路或正常結束）
            # 在「回溯」的時候才加入結果，所以死路會被排到最後

        dfs("JFK")

        return route[::-1]
        # 因為是回溯時加入，順序是反的，最後要 reverse 回來