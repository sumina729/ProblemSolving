import sys

N, M = map(int, sys.stdin.readline().split())
DNA = list(sys.stdin.readline())
A, C ,G ,T = map(int, sys.stdin.readline().split())
count_dic = {'A' : 0, 'C' : 0, 'G':0, 'T' : 0}
r, l = 0, M-1
arr = DNA[r:l]
count = 0

for i in arr:
    count_dic[i] +=1

while(l < N):
    
    count_dic[DNA[l]] +=1

    if(count_dic['A'] >= A and count_dic['C'] >= C and count_dic['G'] >= G and count_dic['T'] >= T) :
        count+=1
    
    count_dic[DNA[r]] -=1
    l+=1
    r+=1


print(count)