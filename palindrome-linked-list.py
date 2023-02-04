class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        stack = []
        while cur:
            stack.append(cur.val)
            cur = cur.next
        cur = head
        while cur:
            value = stack.pop()
            if cur.val != value:
                return False
            cur = cur.next
        return True
