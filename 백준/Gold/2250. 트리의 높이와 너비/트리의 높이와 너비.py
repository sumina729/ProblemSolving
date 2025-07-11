N = int(input())

tree = [ [] for i in range(N+1)]
c_nods = set()
for _ in range(N):
    n1, n2, n3 = map(int,input().split())
    tree[n1] = [n2, n3]
    c_nods.add(n2)
    c_nods.add(n3)


def inorder_traversal(n, d):
    global w, max_d

    if not tree[n][0] == -1: 
        inorder_traversal(tree[n][0], d+1)

    w+=1
    max_d = max(d, max_d)
    tree_w[n] = w
    tree_d[d].append(w)


    if not tree[n][1] == -1:
        inorder_traversal(tree[n][1], d+1)



w = 0
max_d = 0
tree_w = [ 0 for i in range(N+1)]
tree_d = [ [] for i in range(N+1)]

# 부모노드 찾기
for i in range(1, N+1):
    if not i in c_nods:
        p_node = i
        break
# print("부모노드", i)
inorder_traversal(p_node, 1)

# print(tree_w, w)
# print(tree_d, max_d)

# d = 0

ans_d, ans_w = -1, -1
for i in range(1, max_d+1):
    
    w = max(tree_d[i])-min(tree_d[i])+1
    if w > ans_w:
        ans_w = w
        ans_d = i

print(ans_d, ans_w)
        
