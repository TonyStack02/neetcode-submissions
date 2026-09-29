class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        size = 0
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
                size+=1
            else: 
                if size < 1:
                    return False
                elif ((stack[-1] == '(' and ch != ')')
                or (stack[-1] == '[' and ch != ']')
                or (stack[-1] == '{' and ch != '}')):
                    return False
                else:
                    stack.pop()
                    size-=1
        return size==0
