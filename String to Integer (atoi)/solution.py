class Solution:
    def myAtoi(self, s: str) -> int:
        x = 0
        sign = 0
        number = 0
        for i in range(len(s)):
            t = ord(s[i])
            if t==32 and sign==0:
                continue
            elif (t==43 or t==45) and sign==0:
                sign = -1 if t==45 else 1
            elif 48<=t<=57:
                sign = 1 if sign==0 else sign
                x = (10*x) + t - 48
                number = x*sign
                if number>2**31-1:
                    return 2**31-1
                elif number<-2**31:
                    return -2**31
            else:
                return number
        return number