class Solution:
    def reverse(self, x: int) -> int:
        n = 0
        if x==0:
            return 0
        sign = -1 if x<0 else 1
        x = x//sign
        while x!=0:
            tmp = x%10
            n = (n*10) + tmp
            x = x//10
            if n >= 2**31-1:
                return 0            
        return sign*n