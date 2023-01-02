import sys
input = sys.stdin.readline

tmp1 = 1
while(1):
    l,p,v = map(int,input().split())
    cnt = 0

    if l == 0 and p == 0 and v == 0:
        break

    cnt += v//p*l
    v = v%p
    if l > v:
        cnt += v
    else:
        cnt += l
    
    print('Case {}: {}'.format(tmp1,cnt))
    tmp1 += 1