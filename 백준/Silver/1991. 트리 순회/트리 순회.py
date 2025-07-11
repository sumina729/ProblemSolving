N = int(input())

tree = {}

for _ in range(N):
    a1, a2, a3 = input().split()
    tree[a1] = [a2, a3]

'''
전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
'''

def preorder_traversal(a):
    print(a, end="")
    if not tree[a][0] == '.':
        preorder_traversal(tree[a][0])

    if not tree[a][1] == '.':
        preorder_traversal(tree[a][1])

def inorder_traversal(a):
    if not tree[a][0] == '.': 
        inorder_traversal(tree[a][0])

    print(a, end="")
    if not tree[a][1] == '.':
        inorder_traversal(tree[a][1])

def postorder_traversal(a):
    if not tree[a][0] == '.': 
        postorder_traversal(tree[a][0])

    
    if not tree[a][1] == '.':
        postorder_traversal(tree[a][1])

    print(a, end="")

preorder_traversal('A')
print()
inorder_traversal('A')
print()
postorder_traversal('A')