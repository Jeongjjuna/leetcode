class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token == "/":
                num2, num1  = stack.pop(), stack.pop()
                stack.append(int(num1/num2))
            elif token == "*":
                num2, num1  = stack.pop(), stack.pop()
                stack.append(int(num1*num2))
            elif token == "+":
                num2, num1  = stack.pop(), stack.pop()
                stack.append(int(num1+num2))
            elif token == "-":
                num2, num1  = stack.pop(), stack.pop()
                stack.append(int(num1-num2))
        
            else:
                stack.append(int(token))
                
        return stack[-1]