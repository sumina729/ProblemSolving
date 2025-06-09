jumsu_pan = [
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
    [10, 13, 16, 19, 25],
    [20, 22, 24, 25],
    [30, 28, 27, 26, 25],
    [25, 30, 35, 40]
]

mal = [[0,0], [0,0], [0,0], [0,0]]

go_list = list(map(int, input().split()))
ans = 0
def dfs(jumsu, turn):
    global jumsu_pan, mal, go_list, ans

    if turn == 10:
        # print()
        # print()
        # print("점수:", jumsu)
        ans = max(ans, jumsu)
        
        return 
    
    # print(turn, "턴 상황:", mal)
    for i in range(4):
        cp, cn = mal[i]
        if cp > -1: # 턴 끝난 말이 아니면 
    
            nn = cn+go_list[turn]

            # if len(jumsu_pan[cp]) <= nn: # 턴 끝
            #     # print("!!!!도착!!!!!!!!!!!!!1!")
            #     np = -1
            #     nn = -1
            #     new_jumsu = jumsu #점수 그래도
            # else:
            if cp == 0 and nn < 20 and nn%5 == 0: #판 이동해야 하는지 확인
                np = nn//5
                nn = 0
            elif cp == 0 and nn == 20:
                np = 4
                nn = 3
            elif (cp == 1 or cp == 2 or cp == 3) and len(jumsu_pan[cp])-1 <= nn:
                np = 4
                nn = nn+1 - len(jumsu_pan[cp])
            else:
                np = cp

            if  (np == 0 or np == 4) and (len(jumsu_pan[np]) <= nn): # 턴 끝
                # print("!!!!도착!!!!!!!!!!!!!1!")
                np = -1
                nn = -1
                new_jumsu = jumsu #점수 그래도
            else:
                # print(cp, cn, np, nn)
                new_jumsu = jumsu+jumsu_pan[np][nn]
            

                if [np, nn] in mal:
                    # print(np, nn, "겸쳐서 못감")
                    continue
    

            # print(turn, "턴", i, "번말", go_list[turn], "만큼 이동", cp, cn, "->", np, nn," 총점수:", new_jumsu)

            mal[i] = [np, nn]
            dfs(new_jumsu, turn+1)
            mal[i] = [cp, cn]

dfs(0, 0)
print(ans)