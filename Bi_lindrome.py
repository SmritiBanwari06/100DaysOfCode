t = int(input())
for i in range(t):
    n= int(input())
    s = input()
    s1 = set(s)
    if (len(s1)==len(s)):
        print(-1)
    else:
        print(len(s)-2)