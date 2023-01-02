a = input()
n = len(a)
num_0 = 0
num_1 = 0

for i in range(1,n):
    if a[i] != a[i-1]:
        if a[i-1] == '0':
            num_0 += 1
        else:
            num_1 += 1

if a[-1] == '0':
    num_0 += 1
else:
    num_1 += 1

print(min(num_0,num_1))