import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = []
b = []
total = 0

for _ in range(m):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)

if n >= 6:
    if min(a) <= min(b)*6 and min(a) > min(b)*(n%6):
        total = (n//6)*min(a) + (n%6)*min(b)
    elif min(a) <= min(b)*6 and min(a) <= min(b)*(n%6):
        total = (n//6)*min(a) + min(a)
    elif min(a) > min(b)*6:
        total = min(b)*n
else:
    if min(a) < min(b)*n:
        total = min(a)
    else:
        total = min(b)*n

print(total)