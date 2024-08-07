test = []
number6 = [0 for i in range(6)]
N = 0

def bt(count):
    if count == 6:
        for i in range(6): print(number6[i], end =" ")
        print()
        return

    for i in range(N):
        is_set = True
        for ii in range(count):
            if(number6[ii] >= test[i]): is_set = False
        if(is_set):
            # print(count, i)
            number6[count] = test[i]
            bt(count+1)

while(True):
    tmp = input().split()
    if(int(tmp[0]) == 0): break
    N = int(tmp[0])

    test = [0 for i in range(N)]
    for i in range(N):
        test[i] = int(tmp[i+1])
    
    bt(0)
    print()

    