t = int(input())
for i in range(t):
    s = input()
    def vowels(s):
        if s=='a' or s=='e' or s=='i' or s=='o' or s=='u':
            return 1
        else:
            return 0
        
    if len(s)>2:
         for i in range(len(s)-2):
             if vowels(s[i])+vowels(s[i+1])+vowels(s[i+2])==3:
                 print("Happy")
                 break
         else:
             print("Sad")
    else:
        print("sad")