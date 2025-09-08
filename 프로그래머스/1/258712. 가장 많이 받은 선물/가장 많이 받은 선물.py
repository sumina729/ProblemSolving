def solution(friends, gifts):
    answer = 0
    
    p_pan = dict()
    p_list = dict()
    ans_list = dict()
    
    for f1 in friends:
        p_pan[f1] = dict()
        p_list[f1] = [0, 0, 0]
        ans_list[f1] = 0
        for f2 in friends:
            p_pan[f1][f2] = 0
    
    for g in gifts:
        a, b = g.split()
        
        #a -> b 선물 주기
        p_pan[a][b]+=1
        
        p_list[a][0]+=1 #준거 +1
        p_list[b][1]+=1 # 받은거 +=1
    
    for p in p_pan:
        p_list[p][2] = p_list[p][0]-p_list[p][1]
    
    #계산하기
    for f1 in friends:
        for f2 in friends:
            if f1 == f2 or p_pan[f1][f2] == -1 or p_pan[f2][f1] == -1: #같거나 확인 했으면 패스
                continue
                
            print(">",f1, f2)
            if p_pan[f1][f2] > p_pan[f2][f1]:
                ans_list[f1] +=1
            elif p_pan[f1][f2] < p_pan[f2][f1]:
                ans_list[f2] +=1
                
            else: # 같을때, 또는 둘다 0일때
                if p_list[f1][2] > p_list[f2][2]:
                    ans_list[f1] +=1
                elif p_list[f1][2] < p_list[f2][2]:
                    ans_list[f2] +=1
            
            p_pan[f1][f2] = -1
            p_pan[f2][f1] = -1
                
    ans = 0      
    for p in ans_list:
        # print(ans_list[p])
        ans = max(ans, ans_list[p])
    
    return ans