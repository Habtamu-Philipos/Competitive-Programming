class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        leng = 0
        start = node = head
        while start:
            leng +=1
            start = start.next
        middle = leng//2
        counter = 0 
        while node: 
            if  counter == middle:
                return node
            else: 
                counter += 1
                node = node.next
        return None
