t = int(input())
for i in range(t):
    n,x,y = map(int,input().split())
    s = input()
    if('1' not in s) or ('0' not in s):
        print("0")
    else:
        print(min(x,y))