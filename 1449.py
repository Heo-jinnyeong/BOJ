import sys
input = sys.stdin.readline

n, l = map(int, input().split())
lst = list(map(int,input().split()))
lst.sort()
cnt = 1
start = lst[0]
end = lst[0] + l

for i in range(n):
    if start <= lst[i] < end:
        continue
    else:
        cnt += 1
        start = lst[i]
        end = lst[i]+l
print(cnt)