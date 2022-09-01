def check(s):
    if(len(s)<2): return 0

t = int(input())

while(t>0):
    s = input()
    t -= 1
    if(check(s)==0):
        print("NO")
        continue
    if(s[-1]=='6' and s[-2]=='8'):
        print("YES")
    else:
        print("NO")