import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline



def func1(idx,num):
    global cnt
    
    if len(lst_2) == num:
        if sum(lst_2) == s:
            cnt += 1
            return
        return
    
    for i in range(idx,n):
        lst_2.append(lst_1[i])
        func1(i+1,num)
        lst_2.pop()



n,s = map(int,input().split())
cnt = 0
lst_1 = list(map(int,input().split()))
lst_2 = []

for i in range(1,n+1):
    func1(0,i)
print(cnt)