import sys
N = int(sys.stdin.readline())


for i in range(N):
    
    bracket = sys.stdin.readline()
    tmp_num = 0
    is_good = True
    for j in range(len(bracket)):
        if(bracket[j] == "(") : tmp_num+=1
        elif (bracket[j] == ")"): tmp_num-=1

        if(tmp_num<0) :
            is_good = False
            break
    
    if(tmp_num == 0 and is_good): print('YES')
    else: print('NO')
