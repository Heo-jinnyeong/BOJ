# import sys
# input = sys.stdin.readline

# a,b = map(int,input().split())
# cnt = 1

# def Find(a,cnt):
#     # print(a,cnt)
#     if a == b:
#         print(cnt)
#         return

#     if a*2 <= b:
#         Find(a*2,cnt+1)

#         if a*10 + 1 > b:
#             return
        
    
#     if a*10 + 1 <= b:
#         Find(a*10 + 1,cnt+1)
#         return

#     if a*2 > b:
#         if a*10 + 1 < b:
#             Find(a*10 + 1, cnt+1)
            

#         if a*10 + 1 > b:
#             return

#     print(-1)
#     return

# Find(a,cnt)
        

import sys
input = sys.stdin.readline

a,b = map(int,input().split())
cnt = 1

while(a!=b):
    if a==b:
        break
    elif a > b or (b%10 != 1 and b%2 != 0):
        cnt = -1
        break
    elif b%10 == 1:
        cnt += 1
        b = b//10
    elif b%2 == 0:
        cnt += 1
        b = b//2
print(cnt)