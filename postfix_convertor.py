from collections import deque

oprs = {
    '*': '2',
    '/': '2',
    '+': '1',
    '-': '1'
}
brackets = ["(" ,")"]

def read_number(expression, i, num = ""):
    while i < len(expression) and expression[i] not in oprs.keys() and expression[i] not in brackets:
        num += expression[i]
        i += 1
    return num, i

def get_done_with_paranthesis(stack, flag = False):
    operators = deque()
    stack.pop()
    while stack[-1] != "(":
        operators.append(stack.pop())
    stack.pop()
    
    return operators, stack

def convert_infix_to_postfix(expression, postfix = ""):
    stack = deque()
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            num, i = read_number(expression, i)
            postfix += num + " "
            while len(stack) and stack[-1] in oprs.keys() and oprs[stack[-1]] == '2': postfix += stack.pop() + " "
            continue
        else:
            stack.append(expression[i])
        
        if stack[-1] == ")":
            operators, stack = get_done_with_paranthesis(stack)
            for o in operators:
                postfix += o + ' '
                
            while len(stack) and stack[-1] in oprs and oprs[stack[-1]] == '2':
                postfix += stack.pop() + ' '
        
        i += 1
        
    while len(stack): postfix += stack.pop() + ' '
    
    return postfix
            
if __name__ == "__main__":
    for _ in range(int(input())):
        infix_expression = input()
        postfix_expression = convert_infix_to_postfix(infix_expression)
        print (postfix_expression)