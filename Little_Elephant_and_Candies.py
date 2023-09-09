t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    c = list(map(int,input().split()))
    if sum(c) <= b:
        print("Yes")
    else:
        print("No")