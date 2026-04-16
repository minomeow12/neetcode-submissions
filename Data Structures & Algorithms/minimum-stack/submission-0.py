class MinStack:

    def __init__(self):
        self.store = []
        self.minstore = []
        

    def push(self, val: int) -> None:
        self.store.append(val)

        

    def pop(self) -> None:
        self.store.pop()
        

    def top(self) -> int:
        return self.store[-1]
        

    def getMin(self) -> int:
        return min(self.store)
        
