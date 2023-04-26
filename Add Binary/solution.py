class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        na = len(a)
        nb = len(b)
        b = '0' * (na - nb) + b
        carry = 0
        result = ''
        for i in range(na - 1, -1, -1):
            total = int(a[i]) + int(b[i]) + carry
            if total == 0:
                result = '0' + result
                carry = 0
            elif total == 1:
                result = '1' + result
                carry = 0
            elif total == 2:
                result = '0' + result
                carry = 1
            elif total == 3:
                result = '1' + result
                carry = 1
        if carry == 1:
            result = '1' + result
        return result
