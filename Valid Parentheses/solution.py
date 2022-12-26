class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            elif len(stack) == 0:
                return False
            else:
                opened = stack.pop()
                if (i == ')' and opened != '(') or (i == '}' and opened != '{') or (i == ']' and opened != '['):
                    return False
        return len(stack) == 0