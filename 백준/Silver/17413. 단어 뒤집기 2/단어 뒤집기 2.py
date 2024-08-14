import sys
from collections import deque

def set_re_string():
    global re_string
    stack = []
    for j in re_string:
        stack.append(j)
    for j in re_string:
        resert.append(stack.pop())
    re_string = []

s = list(str(sys.stdin.readline()).strip())

resert = []
is_not_string = False
re_string = []
for i in s:
    if i == ' ':
        if re_string:
            set_re_string()
        resert.append(i)
    elif i =='<':
        if re_string:
            set_re_string()
        resert.append(i)
        is_not_string = True
    elif i =='>':    
        resert.append(i)
        is_not_string = False
    elif is_not_string:
        resert.append(i)
    else :
        re_string.append(i)

if re_string:
    set_re_string()

for i in resert:
    print(i, end="")