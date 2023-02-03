class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        dup_value = dict()
        
        while cur:
            if  cur.val in dup_value:
                prev.next = cur.next
                cur = None
            else: 
                dup_value[cur.val] = 1
                prev = cur
            cur = prev.next
        return head
