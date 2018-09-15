gram={'a':"al",'l':"paca",'p':"cp",'c':"pc"}
gramaticas={0:gram}
inp="a"
c=0
b=True
J={0:0}
for i in range(50):

    c=(c*2+(-1)**i)
    print(i+1,2**i)
    J[i+1]=c
supern="110101010110000100001111011001001000001001101110"[::-1]
acu=0
for i in range(len(supern)):
    print("an+"+str(i)+"=an*2^"+str(i)+"+"+str(J[i]))
