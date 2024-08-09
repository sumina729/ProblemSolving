import sys

exp =list(sys.stdin.readline())
stack = []
postfix = []
is_set = False
sum = 0
i = 0

while(True):
    if exp[i] == '\n' : break

    if exp[i].isdigit() and exp[i+1].isdigit() :
        exp[i]= exp[i]+exp[i+1]
        del exp[i+1]
        i -=1

    if exp[i] == '-' and not is_set : 
        exp.insert(i+1, '(')
        is_set = True
    
    if (exp[i+1] == '\n' or exp[i+1] == '-') and is_set : 
        exp.insert(i+1, ')')
        is_set = False
    i +=1

i = 0
while(True):
    if(exp[i] == '\n') : break
    
    if exp[i].isdigit(): 
        postfix.append(exp[i])
    elif exp[i] == '(' :
        stack.append(exp[i])
    elif exp[i] == ')':
        while(True):
            t = stack.pop()
            if t == '(' : break
            else : postfix.append(t)
    else :
        while(True):
            if len(stack) == 0 or stack[-1] == '(': 
                stack.append(exp[i])
                break
            else : postfix.append(stack.pop())
    i+=1

while(len(stack)!= 0):
    postfix.append(stack.pop())

while(len(postfix)!= 0):
    t = postfix[0]
    del postfix[0]
    if t.isdigit() : stack.append(t)
    else : 
        if t == '+' :
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b) + int(a))
        if t == '-' :
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b) - int(a))


    

print(stack.pop())