n = int(input())
group_word_num = 0

for k in range(n):
    str = input()
    is_group = True
    for i in range(len(str)):
        same_char_idx = []

        for j in range(len(str)): #같은 문자 체크
            if(str[i] == str[j]): same_char_idx.append(j)

        for j in range(len(same_char_idx)-1): #연속적인지 체크
            if(same_char_idx[j+1]-same_char_idx[j] > 1): is_group = False
        
    if(is_group): group_word_num +=1

print(group_word_num)
    
