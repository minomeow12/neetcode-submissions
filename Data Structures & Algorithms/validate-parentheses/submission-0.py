class Solution:
    def isValid(self, s: str) -> bool:
        store=[]
        for i in s:
            if i in ["(", "[", "{"]:
                store.append(i)
            if i in [")", "]", "}"]:
                store.pop()
        return store == []