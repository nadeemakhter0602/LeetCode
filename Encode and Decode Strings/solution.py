class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        encoded = ''
        for i in strs:
            l = str(len(i))
            encoded += l + ':' + i
        return encoded

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        decoded = []
        nums = {'1','2','3','4','5','6','7','8','9','0'}
        right = 0
        n = len(str)
        while right < n:
            size = 0
            while right < n and str[right] in nums and str[right] != ':':
                size = size * 10 + ord(str[right]) - ord('0')
                right += 1
            right += 1
            tmp = ''
            while right < n and size > 0:
                tmp += str[right]
                right += 1
                size -= 1
            decoded.append(tmp)
        return decoded
