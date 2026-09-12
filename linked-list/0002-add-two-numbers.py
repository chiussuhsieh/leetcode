# 0002. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# 難度：Medium
# 類型：Linked List

# 思路：
# 兩個數字都用 linked list 表示，且個位數在最前面（反過來存），這剛好跟直式加法
# 從個位數開始往左加的順序一致，可以直接從兩個串列的頭開始邊走邊加，不需要反轉。
#
# 用 dummy node 起手（結果串列的 head 要等算完第一位才知道，跟前面很多題一樣）。
# 用 carry 記錄進位，初始為 0。每一輪：
# - 用條件表達式 val1 = l1.val if l1 else 0（l2 同理），安全處理某個串列已經
#   走完（變成 None）的情況，避免對 None 取 .val 出錯。
# - value = val1 + val2 + carry，這一位該留下的數字是 value % 10，
#   要帶到下一位的新 carry 是 value // 10（單一位數字最大是 9+9+1=19，
#   商最多是 1）。
# - 建立新節點接到結果串列，cur 往前推進。
# - 用 if l1: l1 = l1.next（l2 同理）安全地移動指標，若已經是 None 就不動它，
#   避免對 None 取 .next 出錯，同時保持「走完」用 None 表示的語意一致性
#   （不要用 0 這種容易誤判的值代替 None）。
#
# 迴圈條件是 l1 or l2 or carry：只要任一串列還沒走完，或還有進位沒處理，
# 就要繼續（處理長度不同的兩個串列，以及相加後可能多出一位的情況，例如
# 5+5=10 要多接一個節點存 1）。

# Pattern 筆記：
# 這題是「模擬直式運算」的 pattern，搭配 dummy node 技巧（結果串列起點不確定
# 時的標準解法）。核心是用條件表達式或 if 判斷安全處理「某個輸入已耗盡」的
# 邊界情況，這個技巧在合併多個資料來源、長度不同時反覆用得到。
# 複雜度分析的細節：空間複雜度討論通常會排除「輸出結果本身所需的空間」，
# 只計算演算法額外用掉的輔助空間，這題若不計輸出是 O(1)，若計入輸出則是
# O(max(m,n))，面試時最好主動說明兩種算法的差異。

# Time complexity: O(max(m, n))，m、n 分別為兩個串列的長度
# Space complexity: O(1)（不計輸出結果空間）；若計入輸出結果，則為 O(max(m, n))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # l1 已走完就當作這一位是 0
            val2 = l2.val if l2 else 0
            value = val1 + val2 + carry
            carry = value // 10          # 進位帶到下一位
            singleValue = value % 10     # 這一位留下的數字
            cur.next = ListNode(singleValue)
            cur = cur.next
            if l1:
                l1 = l1.next  # 安全移動，l1 是 None 時保持 None
            if l2:
                l2 = l2.next
        return dummy.next