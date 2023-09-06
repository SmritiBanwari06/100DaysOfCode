t = int(input())
for i in range(t):
    s = int(input())
    c = input()
    ans = c.count("1")
    if(ans%2==0):
        print("YES")
    else:
        print("NO")