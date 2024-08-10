import sys
import copy

lists = [int(sys.stdin.readline()) for i in range(8)]
lists2 = copy.deepcopy(lists)
lists2.sort(reverse=True)
num = 0
num_n = []

for i in range(8):
    
    if lists[i] in lists2[0:5] :
        num+=lists[i]
        num_n.append(i)

print(num)
for i in range(5):
    print(num_n[i]+1, end=" ")