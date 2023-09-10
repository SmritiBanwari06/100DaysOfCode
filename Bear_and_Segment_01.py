t = int(input())
for i in range(t):
    s = input()
    if s.count('1')==0:
        print("NO")
        continue
    count = s.count('1')
    start = s.index('1')
    count1 = s[start:count+start].count('0')
    if(count1):
        print("NO")
    else:
        print("YES")