# t = int(input())
# for i in range(t):
n = int(input())
x  =sum(list(map(int,input().split())))
if x!= n*(n+1)/2:
    print("NO")
else:
    print("YES")
