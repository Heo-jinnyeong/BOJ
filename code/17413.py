s = input()

lst_1 = ''
lst_2 = ''
lst_3 = ''

btn = 0
for i in range(len(s)):
    if btn == 1:
        if s[i] == '>':
            lst_1 += s[i]
            btn = 0
        else:
            lst_1 += s[i]
        continue

    if s[i] == '<':
        btn = 1
        lst_1 += lst_2[::-1]
        lst_2 = ''
        lst_1 += s[i]

    elif s[i] == '>':
        btn = 0
        lst_1 += s[i]
    
    elif s[i] == ' ':
        lst_1 += lst_2[::-1]
        lst_1 += ' '
        lst_2 = ''

    else:
        lst_2 += s[i]
lst_1 += lst_2[::-1]
print(lst_1)