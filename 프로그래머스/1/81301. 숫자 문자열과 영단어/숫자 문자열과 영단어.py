def solution(s):
    
    str_num = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    ]
    
    answer = 0
    
    for i in range(10):
        n_str = str_num[i]
        
        if n_str in s:
            # print(n_str)
            
            s_list = s.split(n_str)
            sum_s = ''
            for t in s_list:
                sum_s = sum_s+t
                sum_s = sum_s+str(i)
            
            sum_s = sum_s[:len(sum_s)-1]
            # print(sum_s)
            
            s = sum_s
                
    return int(s)