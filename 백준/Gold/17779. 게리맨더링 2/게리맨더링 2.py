

N = int(input())
pan = [list(map(int, input().split())) for _ in range(N) ]


# x = 2, y = 5, d1 = 3, d2 = 2
# -> y = 1, x = 4, d1 = 3(왼길이), d2 = 2(오길기)



# d1, d2 ≥ 1, 
# 1 ≤ x < x+d1+d2 ≤ N
# 1 ≤ y-d1 < y < y+d2 ≤ N

ans = sum(sum(pan[i])for i in range(N))
for d1 in range(0, N+1):
    for d2 in range(0, N+1):
        for y in range(0, N):
            for x in range(0, N):
                if -1 < x-d1 < x < x+d2 < N and -1 < y < y+d1+d2 < N:
                    pan_t = [[0 for i in range(N)] for i in range(N)]
                    
                    n_5 = 0
                    cn = 0
                    cn5 = 0
                    cn1 = 0
                    cn2 = 0
                    cn3 = 0
                    cn4 = 0
                    
                    #경계선2
                    for i in range(d2+1): # (x, y), (x+1, y+1), ..., (x+d2, y+d2)
                        if  pan_t[y+i][x+i] == 0:
                            pan_t[y+i][x+i] = 5

                            n_5+= pan[y+i][x+i]
                            cn5+=1

                    
                    #경계선4
                    for i in range(d1+1): #(x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
                        if pan_t[y+d2+i][x+d2-i] == 0:
                            pan_t[y+d2+i][x+d2-i] = 5

                            n_5+= pan[y+d2+i][x+d2-i] 
                            cn5+=1



                    #경계선1
                    for i in range(d1+1): # 1번 경계선: (x, y), (x+1, y-1), ..., (x+d1, y-d1)
                        if pan_t[y+i][x-i] == 0:
                            pan_t[y+i][x-i] = 5

                            n_5+=pan[y+i][x-i]
                            cn5+=1


                            xi = x-i+1

                            while not pan_t[y+i][xi] == 5:
                                pan_t[y+i][xi] = 5

                                n_5+=pan[y+i][xi]
                                cn5+=1

                                xi+=1
                        
                    #경계선3
                    for i in range(d2+1): #(x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
                        if pan_t[y+d1+i][x-d1+i] == 0:
                            pan_t[y+d1+i][x-d1+i] = 5

                            n_5+=pan[y+d1+i][x-d1+i]
                            cn5+=1


                            xi = x-d1+i+1

                            while not pan_t[y+d1+i][xi] == 5:
                                pan_t[y+d1+i][xi] = 5
                                n_5+=pan[y+d1+i][xi]

                                xi+=1

                                
                                cn1+=1


                    

                    n_1 = 0
                    n_2 = 0
                    n_3 = 0
                    n_4 = 0
                    # 선거구

                    #1
                    for r in range(0, y+d1):  
                        c = 0
                        while c <= x and pan_t[r][c] == 0:
                            pan_t[r][c] = 1
                            n_1+=pan[r][c]
                            c+=1

                            cn1+=1

                    #2
                    for r in range(0, y+d2+1): 
                        c = N-1
                        while x< c and pan_t[r][c] == 0:
                            pan_t[r][c] = 2
                            n_2+=pan[r][c]

                            c-=1

                            
                            cn2+=1

                    #3    
                    for r in range(y+d1, N): 
                        c = 0
                        while c < x-d1+d2 and pan_t[r][c] == 0:
                            pan_t[r][c] = 3
                            n_3+=pan[r][c]

                            c+=1

                            
                            cn3+=1

                    #4
                    for r in range(y+d2, N): 
                        c = N-1
                        while  x-d1+d2 <= c and pan_t[r][c] == 0:
                            pan_t[r][c] = 4
                            n_4+=pan[r][c]
                            c-=1

                            
                            cn4+=1
                    
                
                    # print()
                    # print(cn1+cn2+cn3+cn4+cn5, "y, x, d1, d2: ", y, x, d1, d2)
                    # for p in pan_t:
                    #     print(p)

                    max_n = max(n_5, n_4, n_3, n_2, n_1)
                    min_n = min(n_5, n_4, n_3, n_2, n_1)
                    # print(n_5, n_4, n_3, n_2, n_1, "차이:", max_n - min_n)

                    ans = min(max_n - min_n, ans)
print(ans)

