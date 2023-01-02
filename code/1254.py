# import sys
# input = sys.stdin.readline

# a = list(input().strip())

# def Idf(x):
#     tmp = []
#     for i in range(1,len(x)+1):
#         tmp.append(x[-i])
    
#     if tmp == x:
#         return 1
#     else:
#         return 0

# def Idf_2(x):
#     tmp1 = x[:len(x)//2]
#     tmp2 = x[len(x)//2:]

#     if tmp1 == tmp2:
#         return 1
#     else:
#         return 0

# def Idf_3(x):
#     for i in range(0,len(x)-1):
#         if x[i] == x[i+1]:
#             if Idf(x[len(x)-(len(x)-i-1)*2:]):
#                 return (len(x)-i-1)*2 + (len(x) - (len(x)-i-1)*2)*2
#     return len(x)*2 - 1

# if Idf(a):
#     print(len(a))
# else:
#     if Idf_2(a):
#         print(len(a)+1)
#     else:
#         print(Idf_3(a))

s = input()

for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        print(len(s)+i)
        break