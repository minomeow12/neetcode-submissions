class Solution:
    def isValid(self, s: str) -> bool:
        store = {
           ")": "(",
           "]": "[",
           "}": "{"
        }
        record =[]
        for i in s:
            if i in ["[", "{", "("]:
                record.append(i)
            if i in ["]", "}", ")"]:
                if record == []:
                    return False
                elif store[i] != record[-1]:
                    return False
                record.pop()
        return record ==[]