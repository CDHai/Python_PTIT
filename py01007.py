t = int(input())
while(t>0):
    t -= 1
    d = 0
    n,x,m = [float(x) for x in input().split()]
    m /= n
    while(m>=1):
        m = m/(1+x/100)
        d += 1
    print(d)
