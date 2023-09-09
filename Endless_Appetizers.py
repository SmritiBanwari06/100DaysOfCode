t = int(input())
for i in range(t):

    x,y,r = map(int, input().split())
    n = r//30
    x = x+n
    if(x%y==0):
        print(x//y)
    else:
        print((x//y)+1)
