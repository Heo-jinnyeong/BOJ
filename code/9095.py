t = int(input())

def func1(s):
    if s == n:
        lst[n] += 1
        return
    if s+1 <= n:
        func1(s+1)
    if s+2 <= n:
        func1(s+2)
    if s+3 <= n:
        func1(s+3)
    

for _ in range(t):
    n = int(input())
    lst = [0]*(n+1)
    func1(0)
    print(lst[n])