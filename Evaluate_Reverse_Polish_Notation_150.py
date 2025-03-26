# Time:   O(n)
# Space:  O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda x,y : x + y,
            '-': lambda x,y : x - y, 
            '*': lambda x,y : x * y, 
            '/': lambda x,y : int(x / y)
            }
        stack = []
        for token in tokens:
            op = operators.get(token)
            if op:
                first_num = stack.pop()
                second_num = stack.pop()
                result = op(second_num, first_num)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()