class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        memo = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        i = 0
        while(i<len(s)):
            symbol = s[i:i+2]
            if symbol in memo:
                integer+=memo[symbol]
                i+=2
            else:
                integer+=memo[s[i]]
                i+=1
        return integer