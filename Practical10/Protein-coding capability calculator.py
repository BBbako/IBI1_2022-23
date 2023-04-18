def cal(s):
    s = s.upper()
    L = len(s)
    for i in range(L):
        if s[i:i+3] == 'ATG':
            n = i
            while s[n:n+3] != 'TGA':
                n = n+1
            x = n+3-i
    Propotion = x/L
    if Propotion > 0.5:
        print('protein-coding')
    elif Propotion < 0.1:
        print('non-coding')
    else:
        print('unclear')
# example
q='aTgcccctgacccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'
cal(q)
