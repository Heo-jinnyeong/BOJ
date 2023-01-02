import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
lst = list(map(int,input().split()))

lst.sort()

print(lst)