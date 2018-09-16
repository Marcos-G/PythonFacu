gram={'a':"al",'l':"paca",'p':"cp",'c':"pc"}
gramaticas={0:gram}
inp="a"
c=0
b=True
J={1:1}
supern="110101010110000100001111011001001000001001101111"[::-1]

for i in range(len(supern)):
    print("ping")
    print("an+"+str(2**(i))+"=an*"+str(2**(2**(i))))
    c=(c*((2**(2**i))%123456789)+J[2**i])%123456789
    print("pong")
    J[2**(i+1)]=c
    print(len(J))

#supern="11010"[::-1]
acu=0
check=0
for i in range(len(supern)):
    if(supern[i]=='1'):
        check+=2**(i)
        print("an+"+str(2**(i))+"=an*"+str(2**(2**(i)))+"+"+str(J[2**i]))
        print(check)
        acu=(acu*(2**(2**i))+J[2**i])%123456789
        print(acu)
print(acu)
print(check)
