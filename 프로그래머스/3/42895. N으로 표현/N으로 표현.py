def solution(N, number):
    answer = 0
    
    if N == number:
        return 1
    
    dp = [set() for i in range(9)]
    dp[1].add(N)
    
    
    for n in range(2, 9):
        for i in range(1, n):
            j = n-i
            
            print(i, j, n)
            # i랑 j의 조합 찾기  
            for a in dp[i]:
                for b in dp[j]:
                        
                    dp[n].add(int(str(N)*n))
                    
                    dp[n].add(a+b)
                    dp[n].add(a-b)
                    if not b == 0:
                        dp[n].add(a//b)
                    dp[n].add(a*b)
        print(dp[n])           
        if number in dp[n]:
            return n
        
        

    return -1