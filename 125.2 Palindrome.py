import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = re.sub(r'[^\w]|_', '', s)
        if a == a[::-1]:
            return True
        else:
            return False