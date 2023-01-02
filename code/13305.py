import sys
input = sys.stdin.readline

def func1(dist,lst,total):
    print(dist,lst,total)
    if len(lst) == 0:
        print(total)
        return

    min_num = min(lst)
    for i in range(len(lst)):
        if min_num == lst[i]:
            total += sum(dist[i:])*min_num
            func1(dist[:i],lst[:i],total)
            return


n = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))
price.pop()

func1(distance,price,0)