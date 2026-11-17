class Solution:
    def isValid(self, s: str) -> bool:
        valids = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        store = []
        for ch in s:
            if ch in"({[":
                store.append(ch)
            else:
                if not store or store[-1] != valids[ch]:
                    return False
                store.pop()
        return len(store) == 0