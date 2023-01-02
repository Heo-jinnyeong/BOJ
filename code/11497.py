import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))

    lst.sort()
    
    result = 0
    for i in range(2,n):
        result = max(result,abs(lst[i]-lst[i-2]))
    print(result)