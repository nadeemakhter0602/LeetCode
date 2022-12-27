class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        tmp = x
        rev = 0
        while(tmp!=0):
            digit = tmp%10
            rev = (10*rev) + digit
            tmp//=10
        if x==rev:
            return True
        return False