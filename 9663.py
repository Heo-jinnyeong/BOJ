import sys
sys.setrecursionlimit(10**9)

n = int(input())
cnt = 0
lst_1 = [0]*n


def func2(x):
    for i in range(x):
        if lst_1[x] == lst_1[i] or abs(lst_1[x] - lst_1[i]) == x - i:
            return False
    return True

def func1(idx):
    global cnt

    if idx == n:
        cnt += 1
        return

    for i in range(n):
        lst_1[idx] = i
        if func2(idx):
            func1(idx+1)

func1(0)
print(cnt)