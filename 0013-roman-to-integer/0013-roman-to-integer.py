class Solution:
    def romanToInt(self, s: str) -> int:
        valids = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        total = 0
        for i in range(len(s)):
            if i+1<len(s) and valids[s[i]] < valids[s[i+1]]:
                total -= valids[s[i]]
            else:
                total += valids[s[i]]
        return total