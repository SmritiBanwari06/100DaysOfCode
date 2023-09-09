t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    l1 = s.count('R')
    l2 = s.count('G')
    l3 = s.count('B')
    l4 = max(l1,l2,l3)
    print(n-l4)