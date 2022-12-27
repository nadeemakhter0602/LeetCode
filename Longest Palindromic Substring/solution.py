class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = 0, 0
        def util(r,l,s,n):
            start, end = 0, 0
            while r<n and l>=0 and s[r]==s[l]:
                start, end = l, r
                r+=1
                l-=1                
            return start, end
        for i in range(0, n):
            tmp = util(i,i,s,n)
            start, end = tmp if tmp[1]-tmp[0]>end-start else (start, end)
            tmp = util(i+1,i,s,n)
            start, end = tmp if tmp[1]-tmp[0]>end-start else (start, end)
        return s[start:end+1]