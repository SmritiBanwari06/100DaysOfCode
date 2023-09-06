t = int(input())
for i in range(t):
    s = input()
    n = len(s)
    c=0
    for j in range(1,n):
        if s[j-1]!=s[j]:
            c=c+1
    print(c//2) if c%2==0 else print((c+1)//2)