class MyCircularDeque:

    def __init__(self, k: int):
        self.deq = deque([],maxlen=k)
    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.deq.appendleft(value)
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.deq.append(value)
        return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.deq.popleft()
        return True
        
    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.deq.pop()
        return True
    def getFront(self) -> int:
        if self.deq: return self.deq[0]
        return -1
    def getRear(self) -> int:
        if self.deq: return self.deq[-1]
        return -1
    def isEmpty(self) -> bool:
        return True if not self.deq else False
    def isFull(self) -> bool:
         return len(self.deq) == self.deq.maxlen
