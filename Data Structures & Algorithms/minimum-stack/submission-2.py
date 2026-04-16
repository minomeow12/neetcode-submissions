class MinStack:

    def __init__(self):
        self.store = []
        self.minstore = []
        

    def push(self, val: int) -> None:
        self.store.append(val)
        if not self.minstore or val < self.minstore[-1]:
            self.minstore.append(val)

        

    def pop(self) -> None:
        if self.minstore[-1] == self.store[-1]:
            self.minstore.pop()
        self.store.pop()
        

    def top(self) -> int:
        return self.store[-1]
        

    def getMin(self) -> int:
        if self.minstore:
            return self.minstore[-1]
        
