t = int(input())
while(t>0):
    t -= 1
    d = 1
    s = input()
    for i in range (len(s)-1):
        if(ord(s[i])>ord(s[i+1])):
            d = 0
            break
    if(d==1): print("YES")
    else: print("NO")