def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
acu=0
n=32
m=0
while(n>0):
    c=1
    for i in range(m):
        c*=(n-(i+1))
    acu+=c
    m+=1
    n-=2
    print(acu)
print(acu*factorial(32))
