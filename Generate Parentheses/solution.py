class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrack(output, s, n, opened, closed):
            if closed==opened==n:
                output.append(s)
                return
            if closed<opened:
                backtrack(output, s+')', n, opened, closed+1)
            if opened<n:
                backtrack(output, s+'(', n, opened+1, closed)
        backtrack(output, "", n, 0, 0)
        return output