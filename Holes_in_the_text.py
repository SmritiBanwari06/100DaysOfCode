t= int(input())
for i in range(t):
    n= input()
    holes = ['A','B','D','O','P','Q','R']
    h = 0
    for j in n:
        if j in holes:
            if j == 'B':
                h+=2
            else:
                h+=1
    else:
        print(h)

