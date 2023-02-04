class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0 
        carry = 0
        summ = ListNode()
        cur = summ
        while l1 or l2  or carry:
            if not l1:
                i = 0
            else: i = l1.val
            if not l2:
                j = 0
            else: j = l2.val
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                cur.next = ListNode(remainder)
            else: 
                carry = 0
                cur.next = ListNode(s)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return summ.next
