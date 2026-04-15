class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = []

        if len(s) != len(t):
            return False
            
        for i in range(len(s)):
            store.append(s[i])

        for i in range(len(t)):
            if t[i] in store:
                store.remove(t[i])
                
        if store == []:
            return True

        return False
        