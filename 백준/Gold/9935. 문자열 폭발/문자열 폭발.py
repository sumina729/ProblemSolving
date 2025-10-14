word = input()
b_w =  input()

stack = []

for a in  word:
    stack.append(a)

    if stack[-1] == b_w[-1]:
        if  len(stack) >= len(b_w):
            # print(''.join(stack[-len(b_w): ]), b_w)
            if ''.join(stack[-len(b_w): ]) == b_w:
                for _ in range(len(b_w)):
                    stack.pop()


ans = ''.join(stack)
if len(ans) == 0:
    print("FRULA")
else:
    print(ans)
