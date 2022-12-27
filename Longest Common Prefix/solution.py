class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        prefix = ""
        table = set()
        while(True):
            for j in strs:
                n = len(j)
                if i<n and n>0:
                    table.add(j[i])
                else:
                    return prefix
            if len(table)==1:
                prefix+=table.pop()
                i+=1
            else:
                return prefix