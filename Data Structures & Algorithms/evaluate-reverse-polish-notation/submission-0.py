class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [tokens[0]]
        operators = set(["+", "-", "*", "/"])
        i = 1
        while i < len(tokens):
            if tokens[i] in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                res = eval(operand1 + tokens[i] + operand2)
                stack.append(str(int(res)))
            else:
                stack.append(tokens[i])
            i+=1
        return int(stack[-1])