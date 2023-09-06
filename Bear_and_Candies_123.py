t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    x = 1
    while(a>=0 and b>=0):
        a = a-x
        if a<0:
            print("Bob")
            break
        b = b-x-1
        if b<0:
            print("Limak")
            break
        x = x+2
