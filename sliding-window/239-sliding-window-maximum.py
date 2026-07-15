# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/
# 難度: Hard
# Type: Sliding Window (單調遞減佇列 Monotonic Decreasing Deque)

# 思路:
# 用 deque 維護一個「由左到右數值遞減」的候選索引名單,deque 最左邊永遠是目前窗口的最大值索引。
# 每個新元素 nums[right] 加入前,先從 deque 右邊踢除所有數值 <= nums[right] 的索引
# (這些索引對應的數字,只要新元素還在窗口內,就永遠不可能再成為最大值,直接淘汰)。
# 踢除完後把 right 加入 deque 右邊。
# 接著檢查 deque 最左邊的索引是否已經超出窗口左邊界(過期),若是則從左邊踢除。
# 當窗口大小達到 k 時(right >= k-1),deque 最左邊的索引對應的數值就是目前窗口的最大值,加入結果。

# Pattern 筆記:
# 這題的 pattern 是「單調遞減佇列,維護滑動窗口最大值」,
# 下次看到「滑動窗口 + 需要快速取得窗口內最大值(或最小值)」的題目,
# 就可以用 deque 從右邊踢除較小(或較大)元素、從左邊踢除過期元素,達到 O(n) 的效率,
# 比用 heap(O(n log n))更快。

# Time complexity: O(n),每個元素最多被加入、踢除 deque 各一次
# Space complexity: O(k),deque 最多同時存放 k 個索引

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []  # 儲存每個窗口的最大值
        window = deque()  # 存放索引,由左到右對應的數值遞減

        for right in range(len(nums)):  # 右指針逐一往右擴張窗口
            while window and nums[window[-1]] <= nums[right]:  # 從右邊踢除數值 <= 新元素的索引
                window.pop()  # 這些索引已經不可能是最大值了,直接淘汰

            window.append(right)  # 把新索引加入 deque 右邊

            if window[0] < right - k + 1:  # 檢查 deque 最左邊的索引是否已經超出窗口左邊界
                window.popleft()  # 過期了,從左邊踢除

            if right >= k - 1:  # 窗口大小已經達到 k,可以開始記錄最大值
                res.append(nums[window[0]])  # deque 最左邊索引對應的數值就是目前窗口最大值

        return res  # 回傳所有窗口的最大值