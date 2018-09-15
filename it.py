gram={'a':"al",'l':"paca",'p':"cp",'c':"pc"}
gramaticas={0:gram}
inp="a"
c=0
b=True
J={0:0}
for i in range(50):

    c=(c*2+(-1)**i)
    J[i+1]=c
    print(i+1,J[i+1]%123456789)

#supern="110101010110000100001111011001001000001001101111"[::-1]
supern="11110"[::-1]
acu=0
check=0
for i in range(len(supern)):
    if(supern[i]=='1'):
        check+=2**(i)
        print("an+"+str(i+1)+"=an*2^"+str(i+1)+"+"+str(J[i+1]))
        acu=(acu*(2**(i+1))+J[i+1])%123456789
        print(acu)
print(acu)
print(check)
