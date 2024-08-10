import sys
s = str(sys.stdin.readline()).strip()
s=list(s)
s.sort(reverse=True)

for i in s:
    print(i, end="")