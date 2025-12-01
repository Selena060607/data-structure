def postfix(expression):
    stack = []
    tokens = expression.split()
    for token in tokens:
        if token == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif token == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif token == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif token == "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(a / b)
        else:
            stack.append(float(token))
    return stack[0]



# 使用示例
self = "3 4 +"
print(postfix(self))  # 输出结果应为 7.0
