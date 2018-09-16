gram={'a':"al",'l':"paca",'p':"cp",'c':"pc"}
gramaticas={0:gram}
inp="a"
c=0
b=True
J={1:1}
supern="110101010110000100001111011001001000001001101110"[::-1]
acu=0
check=0
for i in range(len(supern)):
    h=pow(2,2**i,123456789)
    c*=h
    c+=J[2**i]
    c=c%123456789
    J[2**(i+1)]=c
    if(supern[i]=='1'):
        check+=2**(i)

        acu*=h
        acu+=J[2**1]
        acu=acu%123456789

print(acu)
