import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

cnt = 0
tmp1 = 0
i = 0
while(1):
    if i+len(b) > len(a):
        break
    if a[i:i+len(b)] == b:
        cnt += 1
        i += len(b)
    else:
        i += 1

print(cnt)