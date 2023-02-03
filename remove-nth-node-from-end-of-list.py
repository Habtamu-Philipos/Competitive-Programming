class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        point1 = dummy
        point2 = head
        count = 0
        while point2 and count < n:
            point2 = point2.next
            count+=1
        while point2:
            point1 = point1.next
            point2 = point2.next
        point1.next = point1.next.next
        return dummy.next
