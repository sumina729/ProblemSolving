inpix = input().strip()

stack = []
postpix = ""


def check(a, b):
    if  a == '(':
        return 1
    elif b == '(':
        return 1
    elif a == '*' or a == '/':
        if b == '+' or b == '-':
            return 1
        else:
            return 0
    else:
        return 0
        


for i in inpix:
    char = str(i)
    if char == '*' or char == '/' or char == '+' or char == '-'  or char == '(': # 연산자이면
        while True:
            if not stack:
                stack.append(char)
                break
            if check(char, stack[-1]):
                stack.append(char)
                break
            else:
                postpix+=stack.pop()

    elif char == ')':
        while stack:
            tmp = stack.pop()
            if(tmp == '('):
                break
            else:
                postpix+=tmp
    else:
        postpix+=char

while stack:
    postpix+=stack.pop()

print(postpix)