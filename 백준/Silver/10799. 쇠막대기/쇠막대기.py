import sys
input = sys.stdin.readline

s = list(str(input()).strip())

stick_n = 0
stack =[]
is_open = True
for i in range(len(s)):
    # print(s[i])
    if s[i] == '(':
        stack.append(i)
        is_open = True
    elif s[i]  == ')':
        if is_open :
            stack.pop()
            stick_n+=len(stack)
        else :
            stack.pop()
            stick_n+=1
        is_open = False
        
print(stick_n)