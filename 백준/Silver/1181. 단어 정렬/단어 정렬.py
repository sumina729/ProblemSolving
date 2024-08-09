import sys
N = int(sys.stdin.readline())
words = list(str(sys.stdin.readline()).strip() for i in range(N))

words = set(words)
words = list(words)
words.sort()
words = sorted(words, key=lambda x : len(x))

for i in words:
    print(i)