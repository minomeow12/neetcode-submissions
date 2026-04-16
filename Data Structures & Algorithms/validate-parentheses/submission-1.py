class Solution:
    def isValid(self, s: str) -> bool:
        store = {
            '(':')',
            '[':']',
            '{':'}',
        }

        record =[]
        for i in s:
            if i in store:
                record.append(i)
            if i in store:
                record.pop()
        return record == []