class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        
        
            
        while i < len(tokens): #to change
            val = tokens[i]
            if val == '+':
                operand_b = stack.pop()
                operand_a = stack.pop()
                stack.append(operand_a + operand_b)
            elif val == '-':
                operand_b = stack.pop()
                operand_a = stack.pop()
                stack.append(operand_a - operand_b)
            elif val == '*':
                operand_b = stack.pop()
                operand_a = stack.pop()
                stack.append(operand_a * operand_b)
            elif val == '/':
                operand_b = stack.pop()
                operand_a = stack.pop()
                stack.append(int(operand_a / operand_b))
            else:
                stack.append(int(val))
            i+=1
        return stack.pop()