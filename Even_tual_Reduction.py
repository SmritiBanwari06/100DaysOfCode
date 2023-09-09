t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    x=0
    for i in s:
        x = s.count(i)
        if(x%2==0):
            x=0
        else:
            x=1
            break
    if(x!=0):
        print("NO")
    else:
        print("YES")        