gram={'a':"al",'l':"paca",'p':"cp",'c':"pc"}
gramaticas={0:gram}
inp="a"
c=0
b=True
J={0:0}
for i in range(50):

    c=(c*2+(-1)**i)
    J[i+1]=c
    print(i+1,J[i+1])

#supern="110101010110000100001111011001001000001001101111"[::-1]
supern="11110"[::-1]
acu=1
check=0
for i in range(len(supern)):
    if(supern[i]=='1'):
        check+=2**(i)
        print("an+"+str(2**(i))+"=an*"+str(2**(2*i))+"+"+str(J[i*2]))
        print(check)
        acu=(acu*(2**(2*i))+J[i*2])
        print(acu)
print(acu)
print(check)
