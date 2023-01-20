class MyQueue:

    def __init__(self):
        self.queue = []
        
    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        self.queue.reverse()
        x= self.queue.pop()
        self.queue.reverse()
        return x
      
    def peek(self) -> int:
        return self.queue[0] 

    def empty(self) -> bool:
        return True if not self.queue else False
