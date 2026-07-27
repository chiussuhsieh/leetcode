# 735 - Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/
# Medium | Stack
# 思路: 用 stack 存目前為止還存活的、往右移動(正數)的小行星。
# 逐一掃描 asteroids:
# 每個新的 asteroid 先假設自己是存活的(alive = True)。
# 只有當 stack 不是空的、stack top 是正數(往右移動)、
# 目前這個 asteroid 是負數(往左移動)、且它還存活時,才會發生碰撞,進入 while 迴圈比較:
#   - 如果目前 asteroid 的絕對值比 stack top 大,stack top 被消滅,pop 掉,
#     繼續用 while 迴圈跟新的 stack top 比較(處理連鎖碰撞)。
#   - 如果兩者絕對值相等,stack top 跟目前 asteroid 都被消滅,
#     把 stack top pop 掉,並把 alive 設成 False。
#   - 如果目前 asteroid 的絕對值比 stack top 小,目前 asteroid 被消滅,
#     把 alive 設成 False,stack top 保持不動。
# while 迴圈結束後(可能是沒有更多碰撞可能,或是目前 asteroid 已經被消滅),
# 如果 alive 還是 True,代表這個 asteroid 撐過了所有碰撞,把它 push 進 stack。
# 最後 stack 裡剩下的就是所有存活的小行星。
# Pattern 筆記: 這題的 pattern 是用 stack 處理「相鄰元素互相消滅」的模擬邏輯,
# 搭配 while 迴圈處理連鎖反應,下次看到「同方向不衝突、只有反方向才會碰撞、
# 且碰撞可能連續發生」這種特徵就用這個方法。
# Time: O(n),雖然有 while 迴圈,但每個元素最多只會被 push 跟 pop 各一次,均攤是 O(n)
# Space: O(n)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            alive = True
            while stack and stack[-1] > 0 and asteroid < 0 and alive:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(asteroid)
        return stack