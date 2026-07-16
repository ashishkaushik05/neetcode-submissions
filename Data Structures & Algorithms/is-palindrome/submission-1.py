class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_chars = set("abcdefghijklmnopqrstuvwxyz0123456789")
        s = s.lower()
        s = "".join(filter(lambda x: x in alnum_chars, s))
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
