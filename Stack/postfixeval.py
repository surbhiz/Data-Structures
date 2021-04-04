class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.item


def domath(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2


def postfix_eval(postfix_str):
    opr_stack = Stack()
    token_list = postfix_str.split()

    for token in token_list:
        if token in '0123456789':
            opr_stack.push(int(token))
        else:
            opr2 = opr_stack.pop()
            opr1 = opr_stack.pop()
            result = domath(token, opr1, opr2)
            opr_stack.push(result)
    return opr_stack.pop()


print(postfix_eval('7 8 + 3 2 + /'))
print(postfix_eval('4 5 6 * +'))
