import sys
from collections import deque

N = int(sys.stdin.readline())
lists = []
for i in range(N):
    lists.append(int(sys.stdin.readline()))

stack = []
stack_list = []
n = 0
number = 1
while True:
    if  number>N:
        break
    elif not len(stack)==0 and stack[-1] == lists[n] :
        stack.pop()
        n+=1
        stack_list.append("-")    
    else :
        stack.append(number)
        number+=1
        stack_list.append("+")

is_good = True
while not len(stack)==0:
    if stack[-1] == lists[n] :
        n+=1
        stack_list.append("-")    
    else : 
        is_good = False
    stack.pop()
    
if is_good : 
    for i in stack_list:
        print(i)
else :
    print("NO")
    