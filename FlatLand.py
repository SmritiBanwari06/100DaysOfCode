t = int(input())
for i in range(t):
    n = int(input())
    x = int(n**0.5)
    c = 0
    while n >0:
        n = n-(int(n**0.5)**2)
        c+=1
    print(c)