class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        new = []
        r = numRows-2
        i = 0
        count = 0
        while(i<len(s)):
            if i%(numRows-1)==0:
                if count%2==0:
                    new.append(s[i:i+numRows])
                else:
                    tmp = ' '+s[i+1:i+r+1][::-1]+' '
                    if len(tmp)<numRows:
                        tmp=' '*(numRows-len(tmp)) + tmp
                    new.append(tmp)
                count+=1
            i+=1
        s = ''
        for i in range(numRows):
            for j in new:
                if i<len(j):
                    if j[i]!=' ':
                        s+=j[i]
        return s