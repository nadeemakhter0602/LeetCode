class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for i in s:
            if i.lower() in 'abcdefghijklmnopqrstuvwxyz01234567890':
                t+=i.lower()
        l = 0
        r = len(t) - 1
        while l < r:
            if t[l] != t[r]:
                return False
            l+=1
            r-=1
        return True