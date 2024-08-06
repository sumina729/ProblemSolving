N = int(input())
for k in range(N):
    number = int(input())

    #각 숫자마다 불린 횟수를 저장
    dp_0 = [0]*41
    dp_1 = [0]*41

    dp_0[0] = 1
    dp_1[0] = 0

    dp_0[1] = 0
    dp_1[1] = 1

    for i in range(2, number+1):
        dp_0[i] = dp_0[i-1] + dp_0[i-2]
        dp_1[i] = dp_1[i-1] + dp_1[i-2]


    print(dp_0[number], dp_1[number])