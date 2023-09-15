t = int(input())
for i in range(t):
    x,y,z = map(int,input().split())
    if(y<=x):
        print("PIZZA")
    elif(z<=x):
        print("BURGER")
    else:
        print("NOTHING")