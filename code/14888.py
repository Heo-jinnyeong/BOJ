import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def func1(idx):
    if len(lst_2) == 6:
        for i in lst_2:
            print(i,end=' ')
        print()
        return
    
    for i in range(idx,lst_1[0]+1):
        lst_2.append(lst_1[i])
        func1(i+1)
        lst_2.pop()

while(1):
    lst_1 = list(map(int,input().split()))
    lst_2 = []
    if lst_1[0] == 0:
        break
    func1(1)
    print()