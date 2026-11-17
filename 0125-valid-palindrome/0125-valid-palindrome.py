class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = ''.join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(valid)-1
        while left<right:
            if valid[left]!=valid[right]:
                return False
            left += 1
            right -= 1
        return True