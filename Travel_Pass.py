t = int(input())
for i in range(t):
    n,a,b = map(int,input().split())
    s= input()
    dp = s.count('0')
    sp = s.count('1')
    print(a*dp+b*sp)