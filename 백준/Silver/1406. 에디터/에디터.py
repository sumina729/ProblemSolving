import sys
input = sys.stdin.readline

word = list(str(input()).strip())
N = int(input())
stack = []

for i in range(N):
    s = list(input().split())

    if s[0] == 'L':
        if word: stack.append(word.pop())

    if s[0] == 'D':
        if stack: word.append(stack.pop())

    if s[0] == 'B':
        if word:  word.pop()

    if s[0] == 'P':
        word.append(s[1])

for i in range(len(word)):
    print(word[i], end="")

for i in range(len(stack)):
    print(stack.pop(), end="")