import random
m=0
h=0
n=20
while(m<1000 and h<1000):
    if(random.randint(0,1)==1):
        m+=1
    gana=True
    for i in range(n):
        if(random.randint(0,1)==0):
            gana=False
            break
    if(gana):
        h+=2**(n-1)
    print(m,h)
