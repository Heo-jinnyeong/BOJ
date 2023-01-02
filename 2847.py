import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

cnt = 0

for i in range(1,n):
    if lst[-i] <= lst[-(i+1)]:
        cnt += lst[-(i+1)] - lst[-i] + 1
        lst[-(i+1)] -= lst[-(i+1)] - lst[-i] + 1

print(cnt)